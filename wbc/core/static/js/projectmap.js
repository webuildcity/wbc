var app = angular.module('wbc', []);

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
}]);

app.controller('DetailsController', ['$scope', '$document', '$http', '$window', 'MapService',
    function($scope, $document, $http, $window, MapService) {
      
    MapService.loadPoly(_polygon);

    $('.map-link').on('click',function(){
         setTimeout(function(){
            MapService.map.invalidateSize();
            if (typeof(_polygon) !== 'undefined') {
               MapService.fitPoly();
            }
        }, 100);
    });
}]);


/** NON ANGULAR **/
$(document).ready(function(){
    moveScroller('.anchor', '#side_content');
});

// function initMap() {
//     // add the map layer and center map
//     map = new L.Map("map",{scrollWheelZoom: false});
//     map.addLayer(new L.TileLayer(_tiles_url,_tiles_opt));
//     map.setView(new L.LatLng(_lat, _lon), 16);

//     // var osmb = new OSMBuildings(map).loadData();

//     var icon = L.icon({
//         iconUrl: _static_url + 'img/icons/gruen.png',
//         iconSize:   [26, 45], // size of the icon width,height
//         iconAnchor: [13, 45], // point of the icon which will correspond to marker's location
//     });

//     var polygonColor = null;
//     var cssPolyRule = getRuleForSelector('.poly');
//     if(cssPolyRule) {
//         polygonColor = cssPolyRule.style.color;
//     }

//     if (typeof(_polygon) !== 'undefined') {
//         var polygonOptions = {
//             weight: 3,
//             color: polygonColor,
//             opacity: 1,
//             fill: true,
//             fillColor: polygonColor,
//             fillOpacity: 0.05
//         };

//         L.multiPolygon(_polygon).setStyle(polygonOptions).addTo(map);
//     }

//     var marker = L.marker([_lat,_lon],{icon: icon}).addTo(map);
//     marker.bindPopup(_address, {
//         autoPanPaddingTopLeft: new L.Point(10,100),
//         autoPanPaddingBottomRight: new L.Point(10,0)
//     }).openPopup();
// }

// $(document).ready(function() {
//     setTimeout('initMap()',100);
// });
