var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('StartpageController', ['$scope', '$document', '$http', '$window',
    function($scope, $document, $http, $window) {
    console.log($scope)
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
        console.log("searhc")
        if($scope.currentSearchTerm) {
            $http({
                method: 'GET',
                url:  '/autocomplete',
                params: {
                    q: $scope.currentSearchTerm
                }
            }).success(function(response) {
                $scope.showDetails = false;
                if (response.results.length) {
                    $scope.data.suggestions = response.results;
                } else {
                    $scope.data.suggestions = [];
                    $scope.noResults = true;


                }
            });
        } else {
            $scope.data.suggestions = [];
        }
    };


    /*
    $scope.focusResult = function(result) {

        $scope.data.currentIdx = $scope.data.results.indexOf(result);
        $scope.data.search = result.name;

        var searchInput = angular.element('#search input');
        searchInput.select();

        if($scope.data.currentPoly !== null) {
            MapService.map.removeLayer($scope.data.currentPoly);
        }

        if(result.polygon){
            var polygonOptions = {
                weight: 3,
                color: '#de6a00',
                opacity: 1,
                fill: true,
                fillColor: '#de6a00',
                fillOpacity: 0.05
            };
            $scope.data.currentPoly = L.multiPolygon(result.polygon)
                .setStyle(polygonOptions)
                .addTo(MapService.map);

            MapService.fitPoly($scope.data.currentPoly);
        }

    };

    $scope.onKeyDown = function(evt) {
        if($scope.data.results.length > 0) {
            if (evt.keyCode == '40') {
                // down arrow
                if($scope.data.currentIdx  < $scope.data.results.length) {
                    $scope.data.currentIdx += 1;
                } else {
                    $scope.data.currentIdx = 0;
                }


            } else if (evt.keyCode == '38') {
                    // up arrow
                if($scope.data.currentIdx !== 0) {
                    $scope.data.currentIdx -= 1;
                }
            }

            var selectedResult = $scope.data.results[$scope.data.currentIdx];
            $scope.focusResult(selectedResult);
        }


    };

    */



}]);