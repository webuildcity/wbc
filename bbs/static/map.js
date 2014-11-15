var app = angular.module('map',[]);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map");
    map.addLayer(new L.TileLayer(_tiles_url + '/{z}/{x}/{y}.png',_tiles_opt));
    map.setView(new L.LatLng(_default_view.lat,_default_view.lon),_default_view.zoom);

    var markerLayer = L.layerGroup().addTo(map);
    var icons = {};

    angular.element('.leaflet-control-attribution').remove();
    angular.element('.leaflet-control-zoom').remove().appendTo(angular.element('#buttons-left'));

    $http.get('/projekte/verfahrensschritte/').success(function(verfahrensschritte) {
        // create icons for verfahrensschritte
        angular.forEach(verfahrensschritte, function(verfahrensschritt, key) {
            icons[verfahrensschritt.pk] = {
                icon: L.icon({
                    iconUrl: verfahrensschritt.icon,
                    iconSize:     [26, 45],
                    iconAnchor:   [13, 45],
                    popupAnchor:  [0, -46]
                }),
                iconUrl: verfahrensschritt.icon,
                hoverIconUrl: verfahrensschritt.hoverIcon
            };
        });

        // create icon for old projects
        icons.old = {
            icon: L.icon({
                iconUrl: '/static/img/icons/grau.png',
                iconSize:     [26, 45],
                iconAnchor:   [13, 45],
                popupAnchor:  [0, -46]
            })
        };

        // get date 3 month ago
        var now = new Date();
        var date = new Date();
        date.setMonth(now.getMonth() - 3);
        var nach = date.toISOString().match(/(\d+-\d+-\d+)/)[0];

        $http.get('/projekte/orte/',{'params': {'nach': nach}}).success(function(geojson) {

            // add points to map
            angular.forEach(geojson.features, function(ort, key) {
                // get the first veroeffentlichung
                var veroeffentlichung = ort.properties.veroeffentlichungen[0];

                // get the pk of the verfahrensschritt
                var vspk = veroeffentlichung.verfahrensschritt.pk;

                // get coordinates
                var lat = ort.geometry.coordinates[1];
                var lon = ort.geometry.coordinates[0];

                // get beginn and ende
                var beginn = new Date(veroeffentlichung.beginn);
                var ende = new Date(veroeffentlichung.ende);

                // see if the veroeffentlichung is in the past create marker
                var marker;
                if (ende < now) {
                    marker = L.marker([lat,lon], {icon: icons.old.icon});
                } else {
                    marker = L.marker([lat,lon], {icon: icons[vspk].icon});

                    // enable hover icon
                    marker.iconUrl = icons[vspk].iconUrl;
                    marker.hoverIconUrl = icons[vspk].hoverIconUrl;

                    marker.on("mouseover", function(e) {
                        e.target._icon.src = this.hoverIconUrl;
                    }).on("mouseout", function(e) {
                        e.target._icon.src = this.iconUrl;
                    });
                }

                // prepare popup
                var d = ende.getDate() + '.' + (ende.getMonth() + 1) + '.' + ende.getFullYear();
                var popuptext = '<p><b>' + veroeffentlichung.verfahrensschritt.verfahren + '</b>';
                popuptext += '<p><i>' + veroeffentlichung.verfahrensschritt.name + '</i>';
                popuptext += ' <a href="/begriffe/#'+ vspk + '" >(?)</a></p>';
                popuptext += '<p>Betrifft Gegend um: ' + ort.properties.adresse + '</p>';
                popuptext += '<p>Verantwortlich: ' + veroeffentlichung.behoerde + '</p>';
                if (beginn == ende) {
                    popuptext += '<p>Zeitpunkt: ' + d + '</p>';
                } else {
                    popuptext += '<p>Beteiligung möglich bis: ' + d + '</p>';
                }
                popuptext += '<p><a href="/orte/' + ort.properties.pk + '" >Details</a></p>';

                // popup to marker
                marker.bindPopup(popuptext, {
                    autoPanPaddingTopLeft: new L.Point(10,100),
                    autoPanPaddingBottomRight: new L.Point(10,0)
                });

                // add marker to layer
                markerLayer.addLayer(marker);
            });
        });
    });

    return {};
}]);

app.controller('MapController',['$scope','MapService',function($scope,MapService) {

    $scope.info = false;
    $scope.help = false;

    $scope.openInfo = function() {
        $scope.info = true;
    };

    $scope.closeInfo = function(event) {
        if (angular.isUndefined(event)){
            $scope.info = false;
        } else {
            $scope.info = !$scope.info;
        }
    };
}]);