app.config(['$locationProvider', function($locationProvider) {
    //html5mode to work with push/pop state in angular
    $locationProvider.html5Mode({
        enabled: true,
      });
}]);

// Searchcontroller to handle everything on the search page, including requests to the server

app.controller('SearchController', ['$scope', '$document', '$http', '$window', '$timeout', '$location', 'MapService',
    function($scope, $document, $http, $window, $timeout, $location, MapService) {


    //models to search through
    $scope.models = {
        'project': 'Projekte',
        'stakeholder': 'Akteure'
    };

    $scope.formData = {};               //Search Form parameters
    $scope.formData.order = '';         //Order of search results
    $scope.formData.tags = [];          //list of tags
    $scope.selectedResult = null;       //currently selected result
    $scope.listView = false;            //switch between views
    $scope.searching = false;           //currently searching?
    $scope.offset = 0;                  //current offset
    $scope.multipoly = [];              //polygon to draw on the map
    $scope.scrolltrigger = false;       
    $scope.activeSearch = false;        
    $scope.searchFocus = false;         //if searchfield is focussed
    $scope.suggestions = [];            //autocomplete suggestions
    $scope.selectedSuggestionIdx = -1;  //selected autocomplete element
    
    //expand filter for mobile search-menu
    $scope.showFilter = false;

    //showFilter for mobile view
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

    //Highlightfunction when mouseover polygon on map
    var highlightFunction = function(id){
        var resultDiv = $('#result-'+id);
        var $parentDiv = $('#search_sidebar');
        resultDiv.toggleClass('selected');
        $parentDiv.scrollTop($parentDiv.scrollTop() + resultDiv.position().top - $parentDiv.height()/2 + resultDiv.height()/2);
        // return null;
    };

    //Mouselistener for polygons
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

    //Search method sends ajax request to server and handles results
    var search = function(data, offset){
        
        $scope.resultLength = 0;
        $scope.searching = true; //currently searching, set to false in succes function
        
        $scope.selectedResult = null; //reset currently selected result

        //reset autocomplete on new search 
        $scope.suggestions = [];
        $scope.selectedSuggestionIdx = -1;
        
        //ajac request to search api
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

                // if offset append results, else clear map and make new resultset
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

                    // add polygon to map if result has one
                    if(result.polygon)  {
                        result.polygon.id = result.pk;
                        poly = MapService.loadPoly(result.polygon, result.pk, highlightFunction);
                        
                        addMouseListener(poly, result);
                        $scope.multipoly.push(result.polygon[0]);
                    }

                    //add buffer areas if project has any
                    if(result.buffer_areas) {
                        result.buffer_areas.forEach(function(area){

                            poly = MapService.loadPoly(area, result.pk, highlightFunction, 'buffer-area');
                            addMouseListener(poly, result);

                            $scope.multipoly.push(area[0]);
                        });                        
                    }
                });
                //add the allResultsPoly to map (contains all polygons of all results)
                allResultPoly = L.multiPolygon($scope.multipoly);
            

                setTimeout(function() {
                    MapService.map.invalidateSize();
                },10);
                
                //zoom to right extend after polygons are drawn (hacky timeout, make this callback)
                if ($scope.multipoly.length > 0) {
                    setTimeout(function() {
                        MapService.map.fitBounds(allResultPoly.getBounds(), {
                            padding: [30, 30]
                        });
                    },100);
                    
                }

                //set the maxzoom, used to pan the map correctly when scrolling thought resultlist
                maxZoom = MapService.map.getZoom();

                // $('.result-content').scroll(resultListScrollHandler);

            } else {
                $scope.results = [];
                $scope.suggestion = response.suggestion;
            }
        });
    };

    //onkeydown method of searchfield, arrows for autocomplete results
    $scope.onKeyDown = function(key){
        if(key.keyCode == '13'){
            if($scope.selectedSuggestionIdx != -1 && $scope.suggestions.length > 0) {
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

        //return to bottom of list if at -2 (-1 is nothing)
        if($scope.selectedSuggestionIdx == -2) {
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

    //AUTOCOMPLETE on input in search field
    var timeoutHandle;
    $scope.onSearchChanged = function() {

        window.clearTimeout(timeoutHandle);

        //Timeout so this only gets fired if no new input in 400ms
        timeoutHandle = window.setTimeout(function() {
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
        }, 400);
        
    };

    //starts the search. handles the offset
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


    //Focusses a polygon, zoominh the map to the extend of the polygon and its buffer areas
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


    // focus result when hovering result in resultlist
    $scope.focusResult = function(result) {

        //timer so only triggers when hovering for more than 400ms
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


    // mouseout for result in resultlist
    $scope.defocusResult = function(result) {

        //reset timer for the animation
        $timeout.cancel(animationTimer);

        if(result.polygon !== undefined) {
             $('.poly-'+result.pk).each(function(i){
                $(this).attr('class', $(this).attr('class').replace('focused-poly',''));
            })
            // $('.poly-'+result.pk).attr('class', 'leaflet-clickable wbc-poly poly-'+result.pk);
            return;
        }
    };

    //when clicked on resultlist entry
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

    //clears the search, TODO: automatic for all fiters
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

    //changes view between list and map view
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
    
    //reorder, value aligns with name for search api
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

    //start standard search when page is loaded
    search($scope.formData);

    // moveScroller($('#search-list-header'), $('.result-content'));
    moveScroller($('.search-anchor'), $('#search_sidebar'));

    //close menu for mobile view on click anywhere else
    $document.on('click', function(e) {
        var target = e.target;
        if (!$(target).is('#side_content') && !$(target).parents().is('#side_content')) {
            $scope.showFilter = false;
            $scope.$apply()
        }
    });
}]);

