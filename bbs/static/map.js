var app = angular.module('bbs',['duScroll']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map", {
        'zoomControl': false,
        'attributionControl': false,
        'scrollWheelZoom': false
    });
    map.addLayer(new L.TileLayer(_tiles_url + '/{z}/{x}/{y}.png',_tiles_opt));
    map.setView(new L.LatLng(_default_view.lat,_default_view.lon),_default_view.zoom);

    var markerLayer = L.layerGroup().addTo(map);
    var icons = {};

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
                    marker = L.marker([lat,lon], {
                        icon: icons[vspk].icon,
                        zIndexOffset: 100
                    });

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

    return {
        map: map
    };
}]);

app.controller('MapController',['$scope','$document','$window','$timeout','$location','$anchorScroll','MapService',function($scope,$document,$window,$timeout,$location,$anchorScroll,MapService) {

    $scope.scroll = true;

    $scope.showInfo = function() {
        // enable scrolling
        angular.element('html').removeClass('locked');
        angular.element('body').removeClass('locked');

        // scroll to info div
        $document.scrollToElement(angular.element('#info'),0, 1000);

        $scope.scroll = true;
    };

    $scope.showMap = function() {
        if ($scope.scroll === true) {
            $scope.scroll = false;

            // scroll to top
            $document.scrollToElement(angular.element('#map'),0, 1000).then(function(){
                // enable mouse scroll on map
                MapService.map.scrollWheelZoom.enable();

                // hide scrollbar
                angular.element('html').addClass('locked');
                angular.element('body').addClass('locked');
            });
        }
    };

    $scope.zoomIn = function(event) {
        $scope.showMap();
        MapService.map.zoomIn();
    };

    $scope.zoomOut = function(event) {
        $scope.showMap();
        MapService.map.zoomOut();
    };

    if ($window.innerWidth < 768) {
        $scope.scroll = false;
        angular.element('html').addClass('locked');
        angular.element('body').addClass('locked');
    }

    MapService.map.on('focus', function() {
        $scope.showMap();
    });

}]);