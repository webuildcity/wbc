// var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('DetailsController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {
      
    MapService.loadPoly(_polygon, undefined, undefined, true);

    $('.map-link').on('click',function(){
         setTimeout(function(){
            MapService.map.invalidateSize();
            if (typeof(_polygon) !== 'undefined') {
                var tempPoly = L.multiPolygon(_polygon);
                MapService.fitPoly(tempPoly);
            }
        }, 100);
    });
    $(document).ready(function(){
        if(location.hash == "#tab_project_map"){
            setTimeout(function(){
                MapService.map.invalidateSize();
                if (typeof(_polygon) !== 'undefined') {
                    var tempPoly = L.multiPolygon(_polygon);
                    MapService.fitPoly(tempPoly);
                }
            }, 100);  
        }
    })
}]);


/** NON ANGULAR **/
$(document).ready(function(){

    moveScroller('.anchor', '#side_content');
    
    /*TAB NAVIGATION MIT URLS */
    var prefix = "tab_";

    var activeTab = $('.main-content-nav a[href=' + location.hash.replace(prefix,'') + ']');
    if (activeTab.length) {
        activeTab.tab('show');
    } else {
        $('.main-content-nav .nav-tabs a:first').tab('show');
    }

    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        e.preventDefault();
        var target = this.href.split('#');
        $('.nav a').filter('.main-content-nav a[href="#'+target[1]+'"]').tab('show');
        window.location.hash = e.target.hash.replace("#", "#" + prefix);
    });

  // navigate to a tab when the history changes
    window.addEventListener("popstate", function(e) {
        var activeTab = $('.main-content-nav a[href=' + location.hash.replace(prefix,'') + ']');
        if (activeTab.length) {
            activeTab.tab('show');
        } else {
            $('.main-content-nav .nav-tabs a:first').tab('show');
        }
        // setTimeout(function() {
        //     window.scrollTo(0, 0);
        // }, 1);
    });

});