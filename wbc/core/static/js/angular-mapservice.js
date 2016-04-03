
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
                setViewOptions.maxZoom = maxZoom;
            }
            map.fitBounds(poly.getBounds(), setViewOptions);
        },

        resetToDefaults: function() {
            map.setView(defaultLocation, defaultZoom,  setViewOptions);
        },

        loadPoly: function(poly, id, highlight, className) {
            if (className === undefined)
                className = ""

            if (typeof(poly) !== 'undefined') {
                var polygonOptions = {
                    className: 'wbc-poly poly-'+id + ' '+ className,
                    weight: 3,
                    fill: true
                };

                var polygon = L.multiPolygon(poly).setStyle(polygonOptions);
                polygonLayer.addLayer(polygon);

                polygon.on('mouseover', function() {
                    $('.poly-'+id).each(function(i){
                        $(this).attr('class', $(this).attr('class') + ' focused-poly');
                    })
                    if (highlight)
                        highlight(id.replace('-buffer', ''));
                    focusedPoly = polygon;
                });
                polygon.on('mouseout', function() {
                    $('.poly-'+id).each(function(i){
                        $(this).attr('class', $(this).attr('class').replace('focused-poly',''));
                    })
                    if (highlight)
                        highlight(id.replace('-buffer', ''));
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
