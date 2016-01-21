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
                        result.polygon.id = result.pk;
                        myPoly = MapService.loadPoly(result.polygon, result.pk, highlightFunction);
                        myPoly.on('click', function() {
                            $scope.selectResult(result);
                        });
                        multipoly.push(result.polygon[0]);
                    }
                });
                allResultPoly = L.multiPolygon(multipoly);
            


                MapService.map.fitBounds(allResultPoly.getBounds(), {
                    padding: [30, 30]
                });
                maxZoom = MapService.map.getZoom();


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
            $scope.onSearchChanged($scope.formData)
        }
    }
    $scope.onSearchChanged = function() {
        var paramData = angular.copy($scope.formData);
        paramData.tags = paramData.tags.toString();
        var params = $.param(paramData);

        $scope.noResults = false;
     
        $window.history.pushState($scope.formData, $scope.q, params);

        search($scope.formData);
    };

    $scope.selectTerm = function(term) {
        $scope.formData.q = term;
        // $scope.onSearchChanged();
    };
    var focusedPoly = null;

    $scope.focusPoly = function(poly) {

        $('.poly-'+poly.pk).attr('class', 'leaflet-clickable wbc-poly focused-poly poly-'+poly.pk);
        var tempPoly = L.multiPolygon(poly.polygon);
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
            $('.poly-'+result.pk).attr('class', 'leaflet-clickable wbc-poly poly-'+result.pk);
            return;
        }
    };

    $scope.selectResult = function(result) {
        $scope.selectedResult = result;
        
        if (result.polygon){
            var tempPoly = L.multiPolygon(result.polygon);
            // ZOOM  TO POLY
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

            console.log("yo")
            setTimeout(function() {
                MapService.map.invalidateSize();
            }, 50);
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
        $scope.onSearchChanged();
    });


    search($scope.formData);

    moveScroller($('#search-list-header'), $('.result-content'));
}]);

/** NON ANGULAR **/
// $(document).resady(function(){
//     moveScroller('.search-anchor', '#search_sidebar');
//     // moveScroller('#type-anchor', '#search_sidebar');
//     $('#map-list-switch').click(function()'result-content'{
//         $('.result-content').toggleClass('hidden');
//     });
// });

