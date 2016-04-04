app.config(['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode({
        enabled: true,
      });
}]);

app.controller('SearchController', ['$scope', '$document', '$http', '$window', '$timeout', '$location', 'MapService',
    function($scope, $document, $http, $window, $timeout, $location, MapService) {


    $scope.models = {
        'project': 'Projekte',
        'stakeholder': 'Akteure'
    };

    $scope.formData = {};
    $scope.formData.order = '';
    $scope.formData.tags = [];
    $scope.selectedResult = null;
    $scope.listView = true;
    $scope.searching = false;
    $scope.offset = 0;
    $scope.multipoly = [];
    $scope.alternatepoly = [];
    // $scope.data = { suggestions: [] };

    var allResultPoly = null;
    var maxZoom = null;
    var animationTimer;

    // var polygonLayer = null;

    var highlightFunction = function(id){
        var resultDiv = $('#result-'+id);
        var $parentDiv = $('#search_sidebar');
        resultDiv.toggleClass('selected');
        $parentDiv.scrollTop($parentDiv.scrollTop() + resultDiv.position().top - $parentDiv.height()/2 + resultDiv.height()/2);
        // return null;
    }

    var search = function(data, offset){
        
        $scope.resultLength = 0;
        $scope.searching = true;
        $scope.selectedResult = null;


        $http({
            method: 'POST',
            url:  '/suche/',
            data: data
        }).success(function(response) {
            // if(polygonLayer != null) {
            //    MapService.map.removeLayer(multipoly);
            // }
            $scope.resultLength = response.length
            $scope.tagFacets = response.facets.fields.tags;
            $scope.entitiesFacets = response.facets.fields.entities;
            $scope.searching = false;
            $scope.offset += 50;

            if (response.results.length>0) {
                if (offset){
                    $scope.results.push.apply($scope.results, response.results);
                } else {
                    MapService.clearPolys();
                    $scope.results = response.results;
                    $scope.multipoly = [];
                }
                $scope.suggestion = null;
                var poly;
                response.results.forEach(function(result){
                    if(result.polygon)  {
                        result.polygon.id = result.pk;
                        poly = MapService.loadPoly(result.polygon, result.pk, highlightFunction);
                        poly.on('click', function() {
                            $scope.selectResult(result);
                        });
                        $scope.multipoly.push(result.polygon[0]);
                    }

                    if(result.buffer_areas) {
                        result.buffer_areas.forEach(function(area){
                            // console.log(area)
                            $scope.alternatepoly.push(area);
                            poly = MapService.loadPoly(area, result.pk, highlightFunction, 'buffer-area');
                            poly.on('click', function() {
                                $scope.selectResult(result);
                            });
                            $scope.multipoly.push(area[0]);
                        });
                        // console.log(result.buffer_areas);
                        
                    }
                });
                allResultPoly = L.multiPolygon($scope.multipoly);
                if ( $scope.alternatepoly.length > 0) {

                // console.log($scope.alternatepoly) 
                // altPoly = L.multiPolygon($scope.alternatepoly);
                }
            


                MapService.map.fitBounds(allResultPoly.getBounds(), {
                    padding: [30, 30]
                });
                maxZoom = MapService.map.getZoom();

                $('.result-content').scroll(resultListScrollHandler);
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

    $scope.onKeyDown = function(key){
        if(key.keyCode == '13'){
            $scope.startSearch(false)
        }
    }


    $scope.onSearchChanged = function() {

        // if($scope.formData.q) {
        //     $scope.isLoading = true;
        //     $http({
        //         method: 'GET',
        //         url:  '/autocomplete',
        //         params: {
        //             q: $scope.formData.q
        //         }
        //     }).success(function(response) {
        //         $scope.isLoading = false;
        //         if (response.results.length) {
        //             $scope.data.suggestions = response.results;
        //         } else {
        //             $scope.data.suggestions = [];
        //             $scope.noResults = true;
        //         }
        //     }).error(function(e){
        //         $scope.isLoading = false;
        //     });
        // } else {
        //     $scope.data.suggestions = [];
        // }

    };

    $scope.startSearch = function(offset) {

        if(offset){
            $scope.formData.offset = $scope.offset
            if(offset === 1)
                $scope.formData.offset  =1;
        } else {
            $scope.offset = 0;
            $scope.formData.offset = 0;
        }
        var paramData = angular.copy($scope.formData);
        paramData.tags = paramData.tags.toString();
        var params = $.param(paramData);

        $scope.noResults = false;
        // $scope.offset = offset || 0;
        
        
        $window.history.pushState($scope.formData, $scope.q, params);

        if(offset){
            // $scope.formData.offset= offset;
            search($scope.formData, true);
        } else {
            search($scope.formData, false);
        }
    };

    $scope.selectTerm = function(term) {
        $scope.formData.q = term;
        // $scope.onSearchChanged();
    };
    var focusedPoly = null;

    $scope.focusPoly = function(result) {

        // $('.poly-'+pk).attr('class', 'leaflet-clickable wbc-poly focused-poly poly-'+poly.pk);
        $('.poly-'+result.pk).each(function(i){
            $(this).attr('class', $(this).attr('class') + ' focused-poly');
        })
        var multipoly = [];
        if(result.buffer_areas) {
            result.buffer_areas.forEach(function(area){
                multipoly.push(area[0]);
            });
            // console.log(result.buffer_areas);
        }
        multipoly.push(result.polygon[0]);

        var tempPoly = L.multiPolygon(multipoly);
        // if (maxZoom < 10){
        //     MapService.fitPoly(tempPoly, maxZoom);
        // } else {
        MapService.fitPoly(tempPoly, maxZoom+1);
        // }
        // ZOOM  TO POLY
        // MapService.map.fitBounds(tempPoly.getBounds(), {
        //     padding: [30, 30]
        // });

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
        animationTimer = $timeout(function () {
            var multipoly = [];
            if(result.polygon !== undefined) {

                $scope.focusPoly(result);
                return;
            }

            if(result.location !== undefined) {
                $scope.focusLocation(result.location);
                return;
            }
        }, 400);
    };

    $scope.defocusResult = function(result) {
        $timeout.cancel(animationTimer);

        if(result.polygon !== undefined) {
             $('.poly-'+result.pk).each(function(i){
                $(this).attr('class', $(this).attr('class').replace('focused-poly',''));
            })
            // $('.poly-'+result.pk).attr('class', 'leaflet-clickable wbc-poly poly-'+result.pk);
            return;
        }
    };

    $scope.selectResult = function(result) {

        $scope.selectedResult = result;
        $scope.$apply();

        if (result.polygon){
            // var tempPoly = L.multiPolygon(result.polygon);
            // ZOOM  TO POLY
            var multipoly = [];
            if(result.buffer_areas) {
                result.buffer_areas.forEach(function(area){
                    multipoly.push(area[0]);
                });
            }
            multipoly.push(result.polygon[0]);

            var tempPoly = L.multiPolygon(multipoly);
            MapService.fitPoly(tempPoly);
        }
    }

    $scope.toggleSelectedItems = function(event){
        $(event.target).siblings('.active-facets').toggleClass('hidden');
    }

    // popstate event listener
    window.addEventListener('popstate', function(e) {
        $scope.formData = e.state;// e.state is equal to the data-attribute of the last image we clicked
        search($scope.formData);
        // $scope.onSearchChanged();
    });
    //SET SEARCH ACCORFING TO URL PARAMS, DIRTY SELECT OF PATH
    if (window.location.pathname.split('/')[2]){
        var result = window.location.pathname.split('/')[2];
        // var result = window.location.pathname.substring(n + 1);

        var param_json= JSON.parse('{"' + decodeURI(result.replace(/&/g, "\",\"").replace(/=/g,"\":\"")) + '"}')
        
        if(param_json['order']){
            $(".order-btn").removeClass("active");
            // TODO: Filter by value and select right button
            // $('.order-btn').value

        }
        $scope.formData.order = param_json['order'];

        if (param_json['tags']){
            var split = param_json['tags'].split(',');
            split.forEach(function(item){
                $scope.formData.tags.push(item);
            });
        }
        // TODO PARSE TAGS AND ENTITIES
        // $scope.formData.entities = param_json['entities[]']
        $scope.formData.q = param_json['q']
    }

    $scope.changeView = function() {
        $scope.listView = !$scope.listView;
        if(!$scope.listView){

            setTimeout(function() {
                MapService.map.invalidateSize();
            }, 50);
        }
    }

    var resultListScrollHandler = function (){
        if($('#result-list').height() < $('.result-content').scrollTop() + $('.result-content').height()+20 && $('.load-more-results').length >0)  {
               $('.result-content').off('scroll', resultListScrollHandler);
               $scope.startSearch($scope.offset);
        }  
    }

    $('.order-btn').click(function(){
        $(".order-btn").siblings(".active").removeClass("active");
        $(this).addClass("active");

        $scope.formData.order = this.value;
        if(this.value[0] != '-') {
            this.value = '-'+this.value;
        } else {
            this.value = this.value.split('-')[1];
        }
        $scope.startSearch(false);
    });

    search($scope.formData);

    moveScroller($('#search-list-header'), $('.result-content'));
    moveScroller($('.search-anchor'), $('#search_sidebar'));

}]);

