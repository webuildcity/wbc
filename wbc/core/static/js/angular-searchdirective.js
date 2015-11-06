app.directive('wbcSearch', function() {
    return {
        restrict: 'E',
        scope: {
            searchTerm: '&'
        },
        controller: function($scope) {
            console.log('controller started...');
        },
        template: '<h1></h1>'
    };
});