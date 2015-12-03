// var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('StartpageController', ['$scope', '$document', '$http', '$window',
    function($scope, $document, $http, $window) {

    $scope.data = { suggestions: [] };
    $scope.noResults = false;
    $scope.currentSearchTerm = "";
    $scope.selectedSuggestion = null;
    $scope.selectedSuggestionIdx = -1;

    $scope.resetSearch = function() {
        $scope.data = { suggestions: [] };
        $scope.noResults = false;
        $scope.currentSearchTerm = "";
        $scope.selectedSuggestion = null;
        $scope.selectedSuggestionIdx = -1;
    };

    $scope.loadDetails = function(result) {
        window.location.href = result.internal_link;
    };

    var focusAutoCompletionResult = function(result) {

        $scope.selectedSuggestionIdx = $scope.data.suggestions.indexOf(result);

    };

    $scope.focusResult = focusAutoCompletionResult;

    $scope.onKeyDown = function(evt) {

        $scope.currentSearchTerm = $scope.currentSearchTerm.trim();

        // tab and enter
        if(evt.keyCode == '9' || evt.keyCode == '13') {

            if($scope.currentSearchTerm.trim().length) {
                if($scope.selectedSuggestionIdx !== -1) {
                    $scope.loadDetails($scope.data.suggestions[$scope.selectedSuggestionIdx]);
                    evt.preventDefault();

                }
            }
        }

        // arrow down
        else if (evt.keyCode == '40') {
            $scope.selectedSuggestionIdx++;
        }

        // arrow up
        else if (evt.keyCode == '38') {
            $scope.selectedSuggestionIdx--;
            evt.preventDefault();
        }

        if ($scope.selectedSuggestionIdx >= $scope.data.suggestions.length) {
            $scope.selectedSuggestionIdx = 0;
        }

        if($scope.selectedSuggestionIdx == -1) {
            $scope.selectedSuggestionIdx = $scope.data.suggestions.length-1;
        }

        if($scope.selectedSuggestionIdx !== -1) {
            var selectedSuggestion = $scope.data.suggestions[$scope.selectedSuggestionIdx];
            if(selectedSuggestion) {
                focusAutoCompletionResult(selectedSuggestion);
                $scope.selectedSuggestion = selectedSuggestion;
            } else {
                $scope.selectedSuggestion = null;
            }
        }
    };

    $scope.onSearchChanged = function() {
        $scope.noResults = false;
        if($scope.currentSearchTerm) {
            $http({
                method: 'GET',
                url:  '/autocomplete',
                params: {
                    q: $scope.currentSearchTerm
                }
            }).success(function(response) {
                if (response.results.length) {
                    $scope.data.suggestions = response.results;
                    console.log($scope.data.suggestions);
                } else {
                    $scope.data.suggestions = [];
                    $scope.noResults = true;


                }
            });
        } else {
            $scope.data.suggestions = [];
        }
    };

}]);

/** SHOW IF SCROLLED **/    
$(document).ready(function(){
    scrollCheck('.top-overlay', '#startpage-content');
})