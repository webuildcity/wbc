var app = angular.module('search', ["checklist-model"]);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);


app.controller('SearchController', ['$scope', '$document', '$http', '$window',
    function($scope, $document, $http, $window) {

    $scope.models = {
        'project': 'Projekte',
        'stakeholder': 'Akteure'
    };

    $scope.formData = {};

    $scope.onSearchChanged = function() {
        $scope.noResults = false;
        console.log($scope.formData);
        // console.log($.param($scope.formData));
        // if($scope.currentSearchTerm) {
            $http({
                method: 'POST',
                url:  '/search/',
                data: $scope.formData
            }).success(function(response) {
                console.log(response);
                console.log($scope.formData);
                // $scope.showDetails = false;
                $scope.resultLength = response.length
                $scope.facets = response.facets.fields.tags;
                $scope.entitiesFacets = response.facets.fields.entities;
                if (response.results.length) {
                    $scope.results = response.results;
                    $scope.suggestion = null;
                    // $scope.showLanding = false;
                } else {
                    $scope.results = [];
                    $scope.suggestion = response.suggestion;
                }
            });
        // } else {
        //     // $scope.results = [];
        //     // $scope.showLanding = true;
        //     // MapService.resetToDefaults();
        // }
    };

    $scope.selectTerm = function(term) {
        $scope.formData.currentSearchTerm = term;
        $scope.onSearchChanged();
    };


}]);