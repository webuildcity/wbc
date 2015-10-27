app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map", {
        'zoomControl': true,
        'scrollWheelZoom': true
    });
    var focusedPoly = undefined;

    var defaultLocation = new L.LatLng(_default_view.lat,_default_view.lon);
    var defaultZoom = _default_view.zoom;

    map.addLayer(new L.TileLayer(_tiles_url,_tiles_opt));
    map.setView(defaultLocation,defaultZoom);

    var setViewOptions = {
        padding: [30, 30],
        maxZoom: 15,
        pan: {
            animate: true,
            duration: 3
        },
        zoom: {
            animate: true
        }
    };

    return {

        map: map,

        focusLocation: function(point) {
            map.setView(point, 15, setViewOptions);
        },

        fitPoly: function(poly) {
            if (poly === undefined){
                poly = focusedPoly;
            }
            map.fitBounds(poly.getBounds(), setViewOptions);
        },

        resetToDefaults: function() {
            map.setView(defaultLocation, defaultZoom,  setViewOptions);
        },

        loadPoly: function(poly) {
            var cssPolyRule = getRuleForSelector('.poly');
            if(cssPolyRule) {
                polygonColor = cssPolyRule.style.color;
            }

            if (typeof(poly) !== 'undefined') {
                var polygonOptions = {
                    weight: 3,
                    color: polygonColor,
                    opacity: 1,
                    fill: true,
                    fillColor: polygonColor,
                    fillOpacity: 0.05
                };

                var polygon = L.multiPolygon(poly).setStyle(polygonOptions);
                polygon.addTo(map);
                focusedPoly = polygon;
            }
        }
    };
}]);
