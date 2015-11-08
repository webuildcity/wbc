
app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map", {
        'zoomControl': true,
        'scrollWheelZoom': true
    });

    var focusedPoly = undefined;
    var polygonLayer= new L.layerGroup();
    map.addLayer(polygonLayer);

    var defaultLocation = new L.LatLng(_default_view.lat,_default_view.lon);
    var defaultZoom = _default_view.zoom;


    var baseTileLayer = new L.TileLayer(_tiles_url,_tiles_opt);

    map.addLayer(baseTileLayer);
    map.setView(defaultLocation,defaultZoom);


    var setViewOptions = {
        padding: [15, 15],
        maxZoom: 20,
        pan: {
            animate: true,
            duration: 0
        },
        zoom: {
            animate: true,
            // duration: 3
        }
    };

    return {

        map: map,

        focusLocation: function(point) {
            map.setView(point, 15, setViewOptions);
        },

        fitPoly: function(poly, maxZoom) {
            // if (poly === undefined){
            //     poly = focusedPoly;
            // }
            var setViewOptions = {
                padding: [15, 15],
                maxZoom: 20,
                pan: {
                    animate: true,
                    duration: 0
                },
                zoom: {
                    animate: true,
                    // duration: 3
                }
            };
            if (maxZoom){
                console.log(maxZoom)
                setViewOptions.maxZoom = maxZoom;
            }
            // console.log(setViewOptions);
            // console.log(setViewOptions.maxZoom);
            map.fitBounds(poly.getBounds(), setViewOptions);
        },

        resetToDefaults: function() {
            map.setView(defaultLocation, defaultZoom,  setViewOptions);
        },

        loadPoly: function(poly, id, highlight) {
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
                    fillOpacity: 0.05,
                    className: 'poly-'+id
                };

                var polygon = L.multiPolygon(poly).setStyle(polygonOptions);
                polygonLayer.addLayer(polygon);

                polygon.on('mouseover', function() {
                    $('.poly-'+id).attr('class', 'leaflet-clickable focused-poly poly-'+id);
                    if (highlight)
                        highlight(id);
                    focusedPoly = polygon;
                });
                polygon.on('mouseout', function() {
                    $('.poly-'+id).attr('class', 'leaflet-clickable poly-'+id);
                    // polygon.setStyle({className: 'poly-'+id});
                    if (highlight)
                        highlight(id);
                    focusedPoly = null;
                });
            }
            return polygon;
        },

        clearPolys: function(){
            map.removeLayer(polygonLayer);
            polygonLayer = new L.layerGroup();
            map.addLayer(polygonLayer);
        }
    };
}]);
