var app = angular.module('map',[]);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller('mapController',['$scope',function($scope) {

    $scope.info = false;
    $scope.help = false;

    $scope.openInfo = function() {
        $scope.info = true;
    };

    $scope.closeInfo = function(event) {

        if (angular.isUndefined(event)){
            $scope.info = false;
        } else {
            $scope.info = !$scope.info;
        }

    };

}]);