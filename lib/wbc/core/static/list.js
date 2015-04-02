var app = angular.module('list',['infinite-scroll']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.directive('list',['ListService',function(ListService) {
    return {
        restrict: 'E',
        templateUrl: _static_url + 'list.html',
        link: function(scope, element, attrs) {
            scope.data = ListService.data;
        }
    };
}]);

app.factory('ListService',['$http',function($http) {

    var idle = true;

    var data = {
        canScroll: true,
        next: '/process/list/',
        rows: []
    };

    function getItems() {
        if (idle) {
            idle = false;
            $http.get(data.next,{params: {page_size: 30}}).success(function(json) {
                data.next = json.next;
                data.rows = data.rows.concat(json.results);
                idle = true;
            });
        }
    }

    getItems();

    return {
        data: data,
        getItems: getItems
    };
}]);

app.controller('FooController',['$scope','ListService',function($scope,ListService) {

    $scope.loadMoreItems = function() {
        ListService.getItems();
    };

}]);
