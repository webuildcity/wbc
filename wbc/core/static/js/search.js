var app = angular.module('search', ["checklist-model"]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('SearchController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {

    $scope.models = {
        'project': 'Projekte',
        'stakeholder': 'Akteure'
    };

    $scope.formData = {};

    var polygonOptions = {
        weight: 3,
        color: '#de6a00',
        opacity: 1,
        fill: true,
        fillColor: '#de6a00',
        fillOpacity: 0.05
    };

    MapService.map.on('zoomend', function() {
        console.log(MapService.map.getBounds() )
        $http({
                method: 'POST',
                url:  '/search/',
                data: {bounds: MapService.map.getBounds()}
            }).success(function(response) {
                if(multipoly != []) {
                   MapService.map.removeLayer(multipoly);
                }
                console.log(response);
                console.log($scope.formData);
                // $scope.showDetails = false;
                $scope.resultLength = response.length
                $scope.facets = response.facets.fields.tags;
                $scope.entitiesFacets = response.facets.fields.entities;
                if (response.results.length) {
                    $scope.results = response.results;
                    $scope.suggestion = null;
                    multipoly=[];
                    response.results.forEach(function(result){
                        console.log(result.polygon)
                        if(result.polygon)  {
                            multipoly.push(result.polygon[0])
                        }
                    });
                    multipoly = L.multiPolygon(multipoly)
                        .setStyle(polygonOptions)
                        .addTo(MapService.map);
                    console.log(multipoly)
                    // MapService.map.fitBounds(multipoly.getBounds(), {
                    //     padding: [30, 30]
                    // });

                    // $scope.showLanding = false;
                } else {
                    $scope.results = [];
                    $scope.suggestion = response.suggestion;
                }
            });
    });


    var multipoly = [];
    $scope.onSearchChanged = function() {
        $scope.noResults = false;
        console.log($scope.formData);
        // console.log($.param($scope.formData));
        // if($scope.currentSearchTerm) {
            $http({
                method: 'POST',
                url:  '/search/',
                data: $scope.formData
            }).success(function(response) {
                if(multipoly != []) {
                   MapService.map.removeLayer(multipoly);
                }
                console.log(response);
                console.log($scope.formData);
                // $scope.showDetails = false;
                $scope.resultLength = response.length
                $scope.facets = response.facets.fields.tags;
                $scope.entitiesFacets = response.facets.fields.entities;
                if (response.results.length) {
                    $scope.results = response.results;
                    $scope.suggestion = null;
                    multipoly=[];
                    response.results.forEach(function(result){
                        console.log(result.polygon)
                        if(result.polygon)  {
                            multipoly.push(result.polygon[0])
                        }
                    });
                    multipoly = L.multiPolygon(multipoly)
                        .setStyle(polygonOptions)
                        .addTo(MapService.map);
                    console.log(multipoly)
                    MapService.map.fitBounds(multipoly.getBounds(), {
                        padding: [30, 30]
                    });

                    // $scope.showLanding = false;
                } else {
                    $scope.results = [];
                    $scope.suggestion = response.suggestion;
                }
            });
        // } else {
        //     // $scope.results = [];
        //     // $scope.showLanding = true;
        //     // MapService.resetToDefaults();
        // }
    };

    $scope.selectTerm = function(term) {
        $scope.formData.currentSearchTerm = term;
        $scope.onSearchChanged();
    };
    var focusedPoly = null;
    $scope.focusPoly = function(poly) {
        if(focusedPoly) {
            MapService.map.removeLayer(focusedPoly);
        }
        var polygonOptions = {
            weight: 3,
            color: '#de6a00',
            opacity: 1,
            fill: true,
            fillColor: '#de6a00',
            fillOpacity: 0.05
        };

        focusedPoly = L.multiPolygon(poly)
            .setStyle(polygonOptions)
            .addTo(MapService.map);
        MapService.map.fitBounds(focusedPoly.getBounds(), {
            padding: [30, 30]
        });
    };


    $scope.focusResult = function(result) {


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
    };




}]);

