var app = angular.module('map',['duScroll']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

// app.factory('MapService',['$http',function($http) {

//     var map = new L.Map("map", {
//         'zoomControl': true,
//         'scrollWheelZoom': true
//     });

//     var defaultLocation = new L.LatLng(_default_view.lat,_default_view.lon);
//     var defaultZoom = _default_view.zoom;

//     map.addLayer(new L.TileLayer(_tiles_url + '/{z}/{x}/{y}.png',_tiles_opt));
//     map.setView(defaultLocation,defaultZoom);

//     var markerLayer = L.layerGroup().addTo(map);
//     var icons = {};

//         // create icon for old projects
//         icons.old = {
//             icon: L.icon({
//                 iconUrl: _static_url + 'img/icons/grau.png',
//                 iconSize:     [26, 45],
//                 iconAnchor:   [13, 45],
//                 popupAnchor:  [0, -46]
//             })
//         };

//         var setViewOptions = {
//           padding: [30, 30],
//           maxZoom: 15,
//           pan: {
//             animate: true,
//             duration: 3
//           },
//           zoom: {
//             animate: true
//           }
//         };

//     return {

//         map: map,

//         focusLocation: function(point) {

//             map.setView(point, 15, setViewOptions);
//         },

//         fitPoly: function(poly) {
//             map.fitBounds(poly.getBounds(), setViewOptions);
//         },

//         resetToDefaults: function() {
//             map.setView(defaultLocation, defaultZoom,  setViewOptions);
//         }
//     };
// }]);


app.controller('StartpageController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {

    $scope.showLanding = true;
    $scope.showDetails = false;

    $scope.data = { suggestions: [] };
    $scope.noResults = false;
    $scope.currentSearchTerm = "";
    $scope.selectedSuggestion = null;
    $scope.selectedSuggestionIdx = -1;
    var focusedPoly = null;
    $scope.details = null;


    var polygonOptions = {
        weight: 3,
        color: '#de6a00',
        opacity: 1,
        fill: true,
        fillColor: '#de6a00',
        fillOpacity: 0.05
    };

    $scope.reset = function() {
        unfocusAll();
        MapService.resetToDefaults();
    };

<<<<<<< HEAD
    $scope.resetSearch = function() {
        $scope.data = { suggestions: [] };
        $scope.noResults = false;
        $scope.currentSearchTerm = "";
        $scope.selectedSuggestion = null;
        $scope.selectedSuggestionIdx = -1;
    };

    $scope.focusLocation = function(location) {
        MapService.focusLocation(location);
    };


    $scope.focusPoly = function(poly) {
        unfocusAll();
        focusedPoly = L.multiPolygon(poly)
            .setStyle(polygonOptions)
            .addTo(MapService.map);
        MapService.map.fitBounds(focusedPoly.getBounds(), {
            padding: [30, 30]
        });
    };

    $scope.detailFocus = function(poly) {
        var bounds = poly.getBounds();
        var diffLat = bounds._northEast.lat - bounds._southWest.lat;
        var diffLng = bounds._northEast.lng - bounds._southWest.lng;
        bounds._southWest.lat = bounds._southWest.lat - diffLat;
        bounds._northEast.lng = bounds._northEast.lng + diffLng*1.5;
        MapService.map.fitBounds(bounds, {
            padding: [0, 0]
        });
    }

    var unfocusAll = function() {
        $scope.showDetails = false;
        if(focusedPoly) {
            MapService.map.removeLayer(focusedPoly);
        }
    }


    var focusAutoCompletionResult = function(result) {

        $scope.selectedSuggestionIdx = $scope.data.suggestions.indexOf(result);

        if(result.polygon !== undefined) {
            $scope.focusPoly(result.polygon);
            return;
        }

        if(result.location !== undefined) {
            $scope.focusLocation(result.location);
            return;
        }

        // nothing to focus
        MapService.resetToDefaults();

        // if poly still focused remove it too
        unfocusAll();

    };

    $scope.focusResult = focusAutoCompletionResult;
    $scope.resetLocation = MapService.resetToDefaults;

    $scope.loadDetails = function(result) {
        // $window.location.pathname = result.internal_link;
       $scope.showDetails = true;
       $scope.detailFocus(focusedPoly);
       $scope.resetSearch();

       $http({
            method: 'GET',
            url:  '/project/projects/'+result.pk,
            params: {
                
            },
        }).success(function(response) {
            console.log(response)
            $scope.details = response;
        });

       

    };

    $scope.onKeyDown = function(evt) {

        $scope.currentSearchTerm = $scope.currentSearchTerm.trim();

        // tab and enter
        if(evt.keyCode == '9' || evt.keyCode == '13') {

            if($scope.currentSearchTerm.trim().length) {
                if($scope.selectedSuggestionIdx !== -1) {
                    $scope.loadDetails($scope.data.suggestions[$scope.selectedSuggestionIdx]);
                    evt.preventDefault();

                }
            }
        }

        // arrow down
        else if (evt.keyCode == '40') {
            $scope.selectedSuggestionIdx++;
        }

        // arrow up
        else if (evt.keyCode == '38') {
            $scope.selectedSuggestionIdx--;
            evt.preventDefault();
        }

        if ($scope.selectedSuggestionIdx >= $scope.data.suggestions.length) {
            $scope.selectedSuggestionIdx = 0;
        }

        if($scope.selectedSuggestionIdx == -1) {
            $scope.selectedSuggestionIdx = $scope.data.suggestions.length-1;
        }

        if($scope.selectedSuggestionIdx !== -1) {
            var selectedSuggestion = $scope.data.suggestions[$scope.selectedSuggestionIdx];
            if(selectedSuggestion) {
                focusAutoCompletionResult(selectedSuggestion);
                $scope.selectedSuggestion = selectedSuggestion;
            } else {
                $scope.selectedSuggestion = null;
            }
        }
    };

    $scope.onSearchChanged = function() {
        $scope.noResults = false;
        if($scope.currentSearchTerm) {
            $http({
                method: 'GET',
                url:  '/autocomplete',
                params: {
                    q: $scope.currentSearchTerm
                }
            }).success(function(response) {
                $scope.showDetails = false;
                if (response.results.length) {
                    $scope.data.suggestions = response.results;
                    $scope.showLanding = false;
                } else {
                    $scope.data.suggestions = [];
                    $scope.noResults = true;

                    MapService.resetToDefaults();
                    unfocusAll();

                }
            });
        } else {
            unfocusAll();
            $scope.data.suggestions = [];
            $scope.showLanding = true;
            MapService.resetToDefaults();
        }
    };


    /*
    $scope.focusResult = function(result) {

        $scope.data.currentIdx = $scope.data.results.indexOf(result);
        $scope.data.search = result.name;

        var searchInput = angular.element('#search input');
        searchInput.select();

        if($scope.data.currentPoly !== null) {
            MapService.map.removeLayer($scope.data.currentPoly);
        }

        if(result.polygon){
            var polygonOptions = {
                weight: 3,
                color: '#de6a00',
                opacity: 1,
                fill: true,
                fillColor: '#de6a00',
                fillOpacity: 0.05
            };
            $scope.data.currentPoly = L.multiPolygon(result.polygon)
                .setStyle(polygonOptions)
                .addTo(MapService.map);

            MapService.fitPoly($scope.data.currentPoly);
        }

    };

    $scope.onKeyDown = function(evt) {
        if($scope.data.results.length > 0) {
            if (evt.keyCode == '40') {
                // down arrow
                if($scope.data.currentIdx  < $scope.data.results.length) {
                    $scope.data.currentIdx += 1;
                } else {
                    $scope.data.currentIdx = 0;
                }


            } else if (evt.keyCode == '38') {
                    // up arrow
                if($scope.data.currentIdx !== 0) {
                    $scope.data.currentIdx -= 1;
                }
            }

            var selectedResult = $scope.data.results[$scope.data.currentIdx];
            $scope.focusResult(selectedResult);
        }


    };

    */



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