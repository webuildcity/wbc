// var app = angular.module('wbc', []);

app.controller('DetailsController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {
      
    var is3d = false;
    $scope.expanded = false;            //mobile view main frame menu

    var poly;
    var polyArray = [_polygon[0]];

    if (_polygon.length >0) {  
        MapService.loadPoly(_polygon, undefined, undefined);
    
        _bufferAreas.forEach(function(area){
            MapService.loadPoly(area, undefined, undefined, 'buffer-area')
            polyArray.push(area[0]);
        });
        poly = L.multiPolygon(polyArray);
        
    } else {
        poly = undefined;
    }

    $scope.ifSmallExpand = function(){
        if(window.matchMedia("(max-width: 768px)").matches){
            $scope.expanded = !$scope.expanded;
        }
    }

    // switch between pdf files
    $scope.openPDF = function(pdf){
        var pdf_viewer = document.getElementById('pdf-viewer');

        // display style change for chrome
        pdf_viewer.style.display = 'none';
        pdf_viewer.data = pdf;
        setTimeout(function() {
            pdf_viewer.style.display = '';
        }, 10);
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

    // TOGGLE TAB IN MAINFRAME
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
    $(".big-page").on('click', '.project-admin', function(ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); 
        var title = $(this).data('title');
        $('#edit-modal .modal-header h3').html(title); // display the modal on url load
        $("#edit-modal .custom-content").load(url, function(response, status) {
 
            if ( status == "error" ) {
                $('#edit-modal .custom-content').html("Fehler!");
            }
            $('#edit-modal').modal();
            $('#edit-modal').modal('show'); // display the modal on url load

            drawMap();
            $( "#edit-modal").unbind( "submit" );
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
                            $('#edit-modal .custom-content').html(data);
                            drawMap();
                        }
                        // $('#edit-modal').modal('hide');
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        if(xhr.status==403) {
                            $('#edit-modal .custom-content').html("Keine Berechtigungen für diese Aktion.");
                        }
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
            $('.wbc-form-datefield-group input').datepicker();
            $('#event-modal').unbind("submit");
            $('#event-modal').on('submit', 'form', function(e){
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
                            $('#event-modal .custom-content').html(data);
                        }
                        // $('#edit-modal').modal('hide');
                    }
                });
            });            
        });
        return false; // prevent the click propagation
    });

    $('.follow-button').on('click', function(){
        $.get($(this).data('url'), function(data) {
            if (data.redirect){
                window.location.href = data.redirect;
                window.location.reload();
            }
        });
    })


    //comments

    $('.comment_reply_link').click(show_reply_form);
    $('#cancel-reply').click(cancel_reply_form);
    $('#div_id_comment textarea').attr('required', true)


    //PHOTO 
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $('#current-photos').on('click', '.delete-photo', function(){
        var parent = $(this).parent();
        $.ajax({
            type: 'POST',
            url: $(this).data('url'),
            success: function(){
                parent.remove();
            }
        });
    });
    // reloads the page after uploading pictures if required
    $('#photo-modal').on('hidden.bs.modal', function(){
        if(reload){
            location.reload(); 
            reload = false;
        }
    });
});

function show_reply_form(event) {
    var $this = $(this);
    var comment_id = $this.data('comment-id');

    $('#id_parent').val(comment_id);
    $('#comment-form').insertAfter($this.closest('.comment'));
};

function cancel_reply_form(event) {
    $('#id_comment').val('');
    $('#id_parent').val('');
    $('#comment-form').appendTo($('#comment-form-wrapper'));
}