//main js file, initilized the app to be used on all sub-pages
//NOTE that we use angular without the routing

var app = angular.module('wbc', ['checklist-model', 'ngAnimate']);

app.config(['$httpProvider', '$interpolateProvider', '$locationProvider', function($httpProvider, $interpolateProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('DefaultController', function() {
});


// load the modal and redirection hhandle for subscribe button
$(document).ready(function(){
    loadModal('#modal', '.modal-button');
    loadLoginModal('#login-modal', '.login-button');
    $('.subscribe-button').on('click', function(){
        $.get($(this).data('url'), function(data) {
            if (data.redirect){
                window.location.href = data.redirect;
                window.location.reload();
            }
        });
    }); 

    var tooltipLocked = false;
    $('.tooltip-container').mouseover(function(e){
        if (!tooltipLocked) {
            $(this).children('.tooltip').css('left', e.offsetX);
            $(this).children('.tooltip').css('top', e.offsetY);
            tooltipLocked = true;        
        }
        // console.log($(this).children('.tooltip'))
    });
    $('.tooltip-container').mouseout(function(e){
        tooltipLocked = false;
    });
}); 
