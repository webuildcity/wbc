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

    // $http.get('/process/processsteps/').success(function(process_steps) {
    //     // create icons for process steps
    //     angular.forEach(process_steps, function(process_step, key) {
    //         icons[process_step.id] = {
    //             icon: L.icon({
    //                 iconUrl: _static_url + process_step.icon,
    //                 iconSize:     [26, 45],
    //                 iconAnchor:   [13, 45],
    //                 popupAnchor:  [0, -46]
    //             }),
    //             iconUrl: _static_url + process_step.icon,
    //             hoverIconUrl: _static_url + process_step.hover_icon
    //         };
    //     });

        // create icon for old projects
        icons.old = {
            icon: L.icon({
                iconUrl: _static_url + 'img/icons/grau.png',
                iconSize:     [26, 45],
                iconAnchor:   [13, 45],
                popupAnchor:  [0, -46]
            })
        };

        // get date
        var now = new Date();

        $http.get('/project/map/').success(function(projects) {

            // add points to map
            angular.forEach(projects, function(project, key) {

                // get coordinates
                var lat = project.point[1];
                var lon = project.point[0];
                    // get the first publication
                var popuptext = '';
                if (project.publication) {
                    var publication = project.publication;


                    if (angular.isUndefined(publication.process_step)) {
                        // set grey marker
                        marker = L.marker([lat,lon], {icon: icons.old.icon});

                        // prepare popup
                        popuptext += '<p>Betrifft Gegend um: ' + project.address + '</p>';
                        popuptext += '<p>Bebauungsplan befindet sich im Verfahren.</p>';
                        popuptext += '<p>Zur Zeit ist keine Bürgerbeteiligung möglich.</p>';
                        popuptext += '<p><a href="' + project.internal_link + '" >Details</a></p>';
                    } else {
                        // get the pk of the process step
                        var process_step_id = publication.process_step.id;

                        // get begin, end, and now
                        var begin = new Date(publication.begin);
                        var end = new Date(publication.end);
                        var now = new Date();

                        if (end < now) {
                            // set grey marker
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
                        popuptext += '<p><b>' + publication.process_step.process_type + '</b>';
                        popuptext += '<p><i>' + publication.process_step.name + '</i>';
                        popuptext += ' <a href="' + publication.process_step.internal_link +  '" >(?)</a></p>';
                        popuptext += '<p>Betrifft Gegend um: ' + project.address + '</p>';
                        popuptext += '<p>Verantwortlich: ' + publication.department + '</p>';
                        if (begin == end) {
                            popuptext += '<p>Zeitpunkt: ' + d + '</p>';
                        } else {
                            popuptext += '<p>Beteiligung möglich bis: ' + d + '</p>';
                        }
                        popuptext += '<p><a href="' + project.internal_link + '" >Details</a></p>';
                    }

                    // popup to marker
                    marker.bindPopup(popuptext, {
                        autoPanPaddingTopLeft: new L.Point(10,100),
                        autoPanPaddingBottomRight: new L.Point(10,0)
                    });

                    // add marker to layer
                    markerLayer.addLayer(marker);
                } else {
                    
                    popuptext += '<p>Betrifft Gegend um: ' + project.address + '</p>';
                    popuptext += '<p><a href="' + project.internal_link + '" >Details</a></p>';

                    marker = L.marker([lat,lon], {icon: icons.old.icon});
                    marker.bindPopup(popuptext, {
                        autoPanPaddingTopLeft: new L.Point(10,100),
                        autoPanPaddingBottomRight: new L.Point(10,0)
                    });

                    markerLayer.addLayer(marker);
                }
            });
        });

    return {
        map: map
    };
}]);

app.controller('MapController',['$scope','$document','$window','$timeout','$location','$anchorScroll','MapService',function($scope,$document,$window,$timeout,$location,$anchorScroll,MapService) {

    $scope.map = true;
    $scope.locked = false;

    $scope.showInfo = function() {
        $timeout(function() {
            $scope.locked = false;
            $scope.map = false;

            // enable mouse scroll on map
            MapService.map.scrollWheelZoom.disable();

            angular.element('html').removeClass('locked');
            angular.element('body').removeClass('locked');

            if ($window.innerWidth >= 768) {
                $document.scrollToElement(angular.element('#info'),0, 1000);
            }
        });
    };

    $scope.showMap = function() {
        if ($scope.locked === false) {
            $timeout(function() {
                $scope.locked = true;
                $scope.map = true;

                if ($window.innerWidth >= 768) {
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

    MapService.map.on('focus', function() {
        $scope.showMap();
    });

}]);