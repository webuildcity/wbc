var app = angular.module('map',['duScroll']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map", {
        'zoomControl': false,
        'scrollWheelZoom': false
    });

    map.addLayer(new L.TileLayer(_tiles_url + '/{z}/{x}/{y}.png',_tiles_opt));
    map.setView(new L.LatLng(_default_view.lat,_default_view.lon),_default_view.zoom);

    var markerLayer = L.layerGroup().addTo(map);
    var icons = {};

    $http.get('/process/process-steps/').success(function(process_steps) {
        // create icons for process steps
        angular.forEach(process_steps, function(process_step, key) {
            icons[process_step.id] = {
                icon: L.icon({
                    iconUrl: _static_url + process_step.icon,
                    iconSize:     [26, 45],
                    iconAnchor:   [13, 45],
                    popupAnchor:  [0, -46]
                }),
                iconUrl: _static_url + process_step.icon,
                hoverIconUrl: _static_url + process_step.hover_icon
            };
        });

        // create icon for old projects
        icons.old = {
            icon: L.icon({
                iconUrl: _static_url + 'img/icons/grau.png',
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

        $http.get('/process/places/',{'params': {'active': true}}).success(function(geojson) {

            // add points to map
            angular.forEach(geojson.features, function(place, key) {
                // get the first publication
                var publication = place.properties.publications[0];

                // get the pk of the process step
                var process_step_id = publication.process_step.id;

                // get coordinates
                var lat = place.geometry.coordinates[1];
                var lon = place.geometry.coordinates[0];

                // get begin and end
                var begin = new Date(publication.begin);
                var end = new Date(publication.end);

                // see if the veroeffentlichung is in the past create marker
                var marker;
                if (end < now) {
                    marker = L.marker([lat,lon], {icon: icons.old.icon});
                } else {
                    marker = L.marker([lat,lon], {
                        icon: icons[process_step_id].icon,
                        zIndexOffset: 100
                    });

                    // enable hover icon
                    marker.iconUrl = icons[process_step_id].iconUrl;
                    marker.hoverIconUrl = icons[process_step_id].hoverIconUrl;

                    marker.on("mouseover", function(e) {
                        e.target._icon.src = this.hoverIconUrl;
                    }).on("mouseout", function(e) {
                        e.target._icon.src = this.iconUrl;
                    });
                }

                // prepare popup
                var d = end.getDate() + '.' + (end.getMonth() + 1) + '.' + end.getFullYear();
                var popuptext = '<p><b>' + publication.process_step.process_type.name + '</b>';
                popuptext += '<p><i>' + publication.process_step.name + '</i>';
                popuptext += ' <a href="' + publication.process_step.link +  '" >(?)</a></p>';
                popuptext += '<p>Betrifft Gegend um: ' + place.properties.address + '</p>';
                popuptext += '<p>Verantwortlich: ' + publication.department.name + '</p>';
                if (begin == end) {
                    popuptext += '<p>Zeitpunkt: ' + d + '</p>';
                } else {
                    popuptext += '<p>Beteiligung möglich bis: ' + d + '</p>';
                }
                popuptext += '<p><a href="' + place.properties.link + '" >Details</a></p>';

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
        // enable mouse scroll on map
        MapService.map.scrollWheelZoom.disable();

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

                // stop video in iframe
                var frame = $('iframe#vimeo-iframe');
                var vidsrc = frame.attr('src');
                frame.attr('src','');
                frame.attr('src', vidsrc);
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