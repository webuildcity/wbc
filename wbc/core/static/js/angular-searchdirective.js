app.directive('wbcSearch', function() {
    return {
        restrict: 'E',
        scope: {
            searchTerm: '&',
            text: '@text'
        },
        templateUrl: '/wbc-searchdirective.html',
        controller: ['$scope', '$http', '$location', function($scope, $http, $location){
            
            $scope.data = { suggestions: [] };
            $scope.isLoading = false;
            $scope.formData = {};

            $scope.selectedSuggestion = null;
            $scope.selectedSuggestionIdx = -1;


            $scope.onSearchChanged = function() {
                if($scope.formData.searchTerm) {
                    $scope.isLoading = true;
                    $http({
                        method: 'GET',
                        url:  '/autocomplete',
                        params: {
                            q: $scope.formData.searchTerm
                        }
                    }).success(function(response) {
                        console.log(response)
                        $scope.isLoading = false;
                        if (response.results.length) {
                            $scope.data.suggestions = response.results;
                        } else {
                            $scope.data.suggestions = [];
                            $scope.noResults = true;
                        }
                    }).error(function(e){
                        $scope.isLoading = false;
                    });
                } else {
                    $scope.data.suggestions = [];
                }
            };

            $scope.submit = function(term){
                window.location = "/suche/?searchTerm="+ term;
            };

            $scope.loadDetails = function(result) {
                window.location.href = result;
            };


            $scope.onKeyDown = function(evt) {


                // tab and enter
                if(evt.keyCode == '9' || evt.keyCode == '13') {
                    console.log($scope.formData.searchTerm)
                    if($scope.selectedSuggestionIdx !== -1) {
                        evt.preventDefault();
                        $scope.loadDetails($scope.data.suggestions[$scope.selectedSuggestionIdx].internal_link);
                    }
                }

                // arrow down
                if (evt.keyCode == '40') {
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
                        // focusAutoCompletionResult(selectedSuggestion);
                        $scope.selectedSuggestion = selectedSuggestion;
                    } else {
                        $scope.selectedSuggestion = null;
                    }
                }
            };

        }]
    };
});