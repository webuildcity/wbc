var app = angular.module('wbc', ["checklist-model"]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('SearchController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {

    console.log(MapService)

    $scope.models = {
        'project': 'Projekte',
        'stakeholder': 'Akteure'
    };

    $scope.formData = {};
    var allResultPoly = null;
    // var polygonLayer = null;
    var polygonColor = null;
    var cssPolyRule = getRuleForSelector('.poly');
    if(cssPolyRule) {
        polygonColor = cssPolyRule.style.color;
    }
    var polygonOptions = {
        weight: 3,
        color: polygonColor,
        opacity: 1,
        fill: true,
        fillColor: polygonColor,
        fillOpacity: 0.05
    };

    var highlightFunction = function(id){
        // console.log(id);
        var resultDiv = $('#result-'+id);
        var $parentDiv = $('#search_sidebar');
        resultDiv.toggleClass('selected');
        $parentDiv.scrollTop($parentDiv.scrollTop() + resultDiv.position().top - $parentDiv.height()/2 + resultDiv.height()/2);

        // return null;
    }

    var search = function(data){
        $http({
            method: 'POST',
            url:  '/suche/',
            data: data
        }).success(function(response) {
            MapService.clearPolys();
            // if(polygonLayer != null) {
            //    MapService.map.removeLayer(multipoly);
            // }
            $scope.resultLength = response.length
            $scope.tagFacets = response.facets.fields.tags;
            $scope.entitiesFacets = response.facets.fields.entities;

            if (response.results.length>0) {
                $scope.results = response.results;
                $scope.suggestion = null;
                var multipoly = [];

                response.results.forEach(function(result){
                    if(result.polygon)  {
                        // console.log(result);
                        result.polygon.id = result.pk;
                        MapService.loadPoly(result.polygon, result.pk, highlightFunction);
                        multipoly.push(result.polygon[0]);
                    }
                });
                allResultPoly = L.multiPolygon(multipoly);
                //     .setStyle(polygonOptions)
                //     .addTo(MapService.map);

                // var highlightFeature = function(){
                //     console.log("yo")
                // }
                // multipoly.on({
                //     mouseover: highlightFeature,
                // });


                MapService.map.fitBounds(allResultPoly.getBounds(), {
                    padding: [30, 30]
                });

                // //scroll things
                // setTimeout(function() {
                //     moveScroller('.tag-anchor', '#search_sidebar');
                //     moveScroller('.region-anchor', '#search_sidebar');
                //     moveScroller('.result-anchor', '#search_sidebar');
                //     // $('.collapse-heading .anchor').click(function(){
                //     //     if($(this).hasClass('fixed-top')){

                //     //         var container = $('#search_sidebar')
                //     //         var scrollTo = $(this).parent();
                //     //         container.animate({
                //     //             scrollTop: scrollTo.offset().top - container.offset().top + container.scrollTop() -70
                //     //         });
                //     //     }
                //     // });
                // }, 100);


            } else {
                $scope.results = [];
                $scope.suggestion = response.suggestion;
            }
        });
    }

    // var multipoly = [];
    $scope.onSearchChanged = function() {
        $scope.noResults = false;
        search($scope.formData);
        // console.log($.param($scope.formData));
        // if($scope.currentSearchTerm) {

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
        // console.log($('.poly-'+poly.pk));

        $('.poly-'+poly.pk).attr('class', 'leaflet-clickable focused-poly poly-'+poly.pk);
        var tempPoly = L.multiPolygon(poly.polygon);
        MapService.map.fitBounds(tempPoly.getBounds(), {
            padding: [30, 30]
        });

        // if(focusedPoly) {
        //     MapService.map.removeLayer(focusedPoly);
        // }
        // var polygonOptions = {
        //     weight: 3,
        //     color: '#de6a00',
        //     opacity: 1,
        //     fill: true,
        //     fillColor: '#de6a00',
        //     fillOpacity: 0.05
        // };

        // focusedPoly = L.multiPolygon(poly)
        //     .setStyle(polygonOptions)
        //     .addTo(MapService.map);
        // MapService.map.fitBounds(focusedPoly.getBounds(), {
        //     padding: [30, 30]
        // });

        // focusedPoly.setStyle({color: '#3E445C', fillColor: '#70D9E8'});
    };


    $scope.focusResult = function(result) {


        if(result.polygon !== undefined) {
            $scope.focusPoly(result);
            return;
        }

        if(result.location !== undefined) {
            $scope.focusLocation(result.location);
            return;
        }

        // nothing to focus
        // MapService.resetToDefaults();

        // if poly still focused remove it too
    };

    $scope.defocusResult = function(result) {


        if(result.polygon !== undefined) {
            // $scope.focusPoly(result);
            $('.poly-'+result.pk).attr('class', 'leaflet-clickable poly-'+result.pk);
            MapService.map.fitBounds(allResultPoly.getBounds(), {
                padding: [30, 30]
            });

            return;
        }

        // if(result.location !== undefined) {
        //     $scope.focusLocation(result.location);
        //     return;
        // }

        // nothing to focus
        // MapService.resetToDefaults();

        // if poly still focused remove it too
    };

    $scope.toggleSelectedItems = function(event){
        $(event.target).siblings('.active-facets').toggleClass('hidden');
    }
    search($scope.formData);
}]);


/** NON ANGULAR **/
$(document).ready(function(){
    moveScroller('.search-anchor', '#search_sidebar');
    // moveScroller('#type-anchor', '#search_sidebar');
});

