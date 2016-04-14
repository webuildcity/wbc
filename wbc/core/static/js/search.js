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
    $scope.listView = false;
    $scope.searching = false;
    $scope.offset = 0;
    $scope.multipoly = [];
    $scope.scrolltrigger = false;
    $scope.activeSearch = false;
    $scope.searchFocus = false;
    $scope.suggestions = [];
    $scope.selectedSuggestionIdx = -1;
    // $scope.data = { suggestions: [] };
    
    //expand filter for mobile search-menu
    $scope.showFilter = false;
    $scope.$watch('showFilter', function(){
        if (!$scope.showFilter)
            $('#filter-container').slideUp(200);
        else
            $('#filter-container').slideDown(200);
    });

    var allResultPoly = null;
    var maxZoom = null;
    var animationTimer;
    var changeDelay = 300;
    // var polygonLayer = null;

    var highlightFunction = function(id){
        var resultDiv = $('#result-'+id);
        var $parentDiv = $('#search_sidebar');
        resultDiv.toggleClass('selected');
        $parentDiv.scrollTop($parentDiv.scrollTop() + resultDiv.position().top - $parentDiv.height()/2 + resultDiv.height()/2);
        // return null;
    };

    var addMouseListener = function(poly, result){
        var delay = 300;
        var timer = null;

        poly.on('click', function() {
            $scope.selectResult(result);
        });

        $(poly).on('mouseover', function() {
            timer = setTimeout(function(){
                $scope.selectedResult = result;
                $scope.$apply();
                
            }, delay);
        }).on('mouseleave', function(){
            clearTimeout(timer);
        });
    }

    var search = function(data, offset){
        
        $scope.resultLength = 0;
        $scope.searching = true;
        $scope.selectedResult = null;
        $scope.suggestions = [];
        $scope.selectedSuggestionIdx = -1;
        $http({
            method: 'POST',
            url:  '/suche/',
            data: data
        }).success(function(response) {
       
            $scope.resultLength = response.length
            $scope.tagFacets = response.facets.fields.tags;
            $scope.entitiesFacets = response.facets.fields.entities;
            $scope.searching = false;
            $scope.offset += 50;

            // Set activeSearch for clear search button, TODO: automatic for all filters
            if($scope.formData.q || $scope.formData.tags.length > 0){
                $scope.activeSearch = true;
            } else {
                $scope.activeSearch = false;
            }

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
                        
                        addMouseListener(poly, result);
                        $scope.multipoly.push(result.polygon[0]);
                    }

                    if(result.buffer_areas) {
                        result.buffer_areas.forEach(function(area){

                            poly = MapService.loadPoly(area, result.pk, highlightFunction, 'buffer-area');
                            addMouseListener(poly, result);

                            $scope.multipoly.push(area[0]);
                        });                        
                    }
                });
                allResultPoly = L.multiPolygon($scope.multipoly);
            

                setTimeout(function() {
                    MapService.map.invalidateSize();
                },0);
                
                if ($scope.multipoly.length > 0) {
                    setTimeout(function() {
                        MapService.map.fitBounds(allResultPoly.getBounds(), {
                            padding: [30, 30]
                        });
                    },100);
                    
                }
                maxZoom = MapService.map.getZoom();

                // $('.result-content').scroll(resultListScrollHandler);

            } else {
                $scope.results = [];
                $scope.suggestion = response.suggestion;
            }
        });
    }

    $scope.onKeyDown = function(key){
        if(key.keyCode == '13'){
            if($scope.selectedSuggestionIdx !== -1 && $scope.suggestions.length > 0) {
                key.preventDefault();
                $scope.selectTerm($scope.suggestions[$scope.selectedSuggestionIdx].name);
            }
            $scope.startSearch(false)
            $scope.suggestions = [];
            $scope.selectedSuggestionIdx = -1;
        }

        // arrow down
        if (key.keyCode == '40') {
            $scope.selectedSuggestionIdx++;
        }

        // arrow up
        else if (key.keyCode == '38') {
            $scope.selectedSuggestionIdx--;
            key.preventDefault();
        }

        if ($scope.selectedSuggestionIdx >= $scope.suggestions.length) {
            $scope.selectedSuggestionIdx = 0;
        }

        if($scope.selectedSuggestionIdx == -1) {
            $scope.selectedSuggestionIdx = $scope.suggestions.length-1;
        }

        if($scope.selectedSuggestionIdx !== -1) {
            var selectedSuggestion = $scope.suggestions[$scope.selectedSuggestionIdx];
            if(selectedSuggestion) {
                // focusAutoCompletionResult(selectedSuggestion);
                $scope.selectedSuggestion = selectedSuggestion;
            } else {
                $scope.selectedSuggestion = null;
            }
        }
    }

    $scope.setIndex = function(index){
        $scope.selectedSuggestionIdx = index;
    }

    //AUTOCOMPLETE HERE?
    $scope.onSearchChanged = function() {

        setTimeout(function() {}, 10);
        if($scope.formData.q) {
            $scope.isLoading = true;
            $http({
                method: 'GET',
                url:  '/autocomplete',
                params: {
                    q: $scope.formData.q
                }
            }).success(function(response) {
                $scope.isLoading = false;
                if (response.results.length) {
                    $scope.suggestions = response.results;
                } else {
                    $scope.suggestions = [];
                    $scope.noResults = true;
                }
            }).error(function(e){
                $scope.isLoading = false;
            });
        } else {
            $scope.suggestions = [];
            $scope.selectedSuggestionIdx = -1;
        }

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
        
        $window.history.pushState($scope.formData, $scope.q, params);

        if(offset){
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

        $('.poly-'+result.pk).each(function(i){
            $(this).attr('class', $(this).attr('class') + ' focused-poly');
        });

        var multipoly = [];
        if(result.buffer_areas) {
            result.buffer_areas.forEach(function(area){
                multipoly.push(area[0]);
            });
        }
        multipoly.push(result.polygon[0]);

        var tempPoly = L.multiPolygon(multipoly);

        MapService.fitPoly(tempPoly, maxZoom+1);
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

    $scope.clearSearch = function(){
        $scope.formData = {};
        $scope.formData.order = '';
        $scope.formData.tags = [];
        $scope.offset = 0;
        $scope.startSearch(false);
    }

    $scope.toggleSelectedItems = function(event){
        $(event.target).siblings('.active-facets').toggleClass('hidden');
    };

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
    };

    $scope.changeView = function() {
        $scope.listView = !$scope.listView;
        if(!$scope.listView){

            setTimeout(function() {
                MapService.map.invalidateSize();
            }, 50);
        }
    };


    //infinite scroll for resultlist
    var resultListScrollHandler = function (){
        if($('#result-list').height() < $('#list').scrollTop() + $('#list').height()+20 && $('.load-more-results').length >0)  {
            // $('#list').off('scroll', resultListScrollHandler);
            if (!$scope.searching)
                $scope.startSearch($scope.offset);
        }  
    };
    $('#list').scroll(resultListScrollHandler);
    
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

    // moveScroller($('#search-list-header'), $('.result-content'));
    moveScroller($('.search-anchor'), $('#search_sidebar'));

    // function moveScroller2(anchorSelector, scrollerSelector) {
    //     var move = function() {
    //         var scrollTop = $(scrollerSelector).scrollTop();
    //         var offset = $(anchorSelector).offset();
    //         var offsetTop = 0;
    //         if(offset !== undefined) {
    //             offsetTop = offset.top;
    //         }

    //         var anchor = $(anchorSelector);
    //         if(scrollTop > offsetTop) {
    //             anchor.addClass('fixed-top');
    //             $scope.scrolltrigger = true;
    //         } else {
    //             anchor.removeClass('fixed-top');
    //             $scope.scrolltrigger = false;

    //         }
    //     };

    //     $(scrollerSelector).scroll(move);
    //     move();
    // }
    // moveScroller2($('.search-anchor'), $('#search_sidebar'));


    $document.on('click', function(e) {
        var target = e.target;
        if (!$(target).is('#side_content') && !$(target).parents().is('#side_content')) {
            $scope.showFilter = false;
            $scope.$apply()
        }
    });
}]);

