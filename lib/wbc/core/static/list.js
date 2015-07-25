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
            scope.entity = attrs.entity;
            scope.data = ListService.data;
        }
    };
}]);

app.factory('ListService',['$http',function($http) {

    var idle = true;

    var data = {};

    function getItems() {
        if (idle) {
            var params = {};
            if (data.search.length != 0) params.search = data.search;

            idle = false;
            $http.get(data.next,{params: params}).success(function(json) {
                data.next = json.next;
                data.count = json.count;
                data.rows = data.rows.concat(json.results);
                if (data.next) idle = true;
            });
        }
    }

    function search() {
        idle = true;
        data.next = '/projects/list/';
        data.rows = [];
        getItems();
    }

    function reset() {
        idle = true;
        data.search = '';
        data.next = '/projects/list/';
        data.rows = [];
        getItems();
    }

    reset();

    return {
        data: data,
        getItems: getItems,
        search: search,
        reset: reset
    };
}]);

app.controller('ListController',['$scope','ListService',function($scope,ListService) {

    $scope.data = ListService.data;

    $scope.loadMoreItems = function() {
        ListService.getItems();
    };

    $scope.search = function() {
        ListService.search();
    };

    $scope.reset = function() {
        ListService.reset();
    };

}]);
