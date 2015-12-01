// var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('DetailsController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {
      
    var is3d = false;

    var poly;
    if (_polygon.length >0) {  
        poly = L.multiPolygon(_polygon);;
        MapService.loadPoly(_polygon, undefined, undefined, true);
    } else {
        poly = undefined;
    }

    $('.map-link').on('click',function(){
         setTimeout(function(){
            MapService.map.invalidateSize();
            if (_polygon.length >0) {
                MapService.fitPoly(poly);
            // } else {
            //     MapService.fitLocation()
            }
        }, 100);
    }); 
    $('.3d-link').on('click',function(){
         setTimeout(function(){
            if(!is3d)
                wbc3d('#vizicities-viewport', [_lat,_lon], poly);
                is3d = true;
        }, 10);
    });
    $(document).ready(function(){
        if(location.hash == "#/project_map"){
            setTimeout(function(){
                MapService.map.invalidateSize();
                if (_polygon.length >0) {
                    MapService.fitPoly(poly);
                }
            }, 100);  
        }
        if(location.hash == "#/3d"){
            setTimeout(function(){
                if(!is3d)
                    wbc3d('#vizicities-viewport', [_lat,_lon], poly);    
                    is3d = true;
            }, 10); 
        } 
    })
}]);


/** NON ANGULAR **/
$(document).ready(function(){

    moveScroller('.anchor', '#side_content');
    
    /*TAB NAVIGATION MIT URLS */
    var prefix = "/";

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
    });


    // MODAL
    $(".project-admin").click(function(ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); 
        $("#edit-modal .modal-content").load(url, function() {
            console.log(url);
            $('#edit-modal').modal();
            $('#edit-modal').modal('show'); // display the modal on url load
            drawMap();
            $('#edit-modal').on('submit', 'form', function(e){
                e.preventDefault();
                $.ajax({ 
                    type: $(this).attr('method'), 
                    url: url, 
                    data: $(this).serialize(),
                    context: this,
                    success: function(data, status) {
                        if (data.redirect){
                            window.location.href = data.redirect;
                        }
                        else {
                            // console.log(data);
                            $('#edit-modal .modal-content').html(data);
                            drawMap();
                        }
                        // $('#edit-modal').modal('hide');
                    }
                });
            });
        });
        return false; // prevent the click propagation
    

    });

    $(".event-admin").click(function(ev) { // for each edit contact url
        $(".nav-pills").find(".active").removeClass("active");
        $(this).parent().addClass("active");
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); 

        $("#event-modal .custom-content").load(url, function() {
            $('#event-modal').on('submit', 'form', function(e){
                e.preventDefault();
                $.ajax({ 
                    type: $(this).attr('method'), 
                    url: url, 
                    data: $(this).serialize(),
                    context: this,
                    success: function(data, status) {
                        console.log(data);
                        if (data.redirect){
                            window.location.href = data.redirect;
                        }
                        else {
                            console.log(data);
                            $('#event-modal .custom-content').html(data);
                        }
                        // $('#edit-modal').modal('hide');
                    }
                });
            });            
        });
        return false; // prevent the click propagation
    });



});