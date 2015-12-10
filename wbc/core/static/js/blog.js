// var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('BlogController', ['$scope', '$document', '$http', '$window',
    function($scope, $document, $http, $window) {


}]);


// MODAL
$(document).ready(function() {

    $(".blog-admin").click(function(ev) {
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); 
        $('#edit-modal .modal-header h3').html(url); // display the modal on url load
        $("#edit-modal .custom-content").load(url, function() {
            $('#edit-modal').modal();
            $('#edit-modal').modal('show'); // display the modal on url load
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
                        }
                    }
                });
            });
        });
        return false; // prevent the click propagation
    });
});