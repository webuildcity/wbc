app.factory('MapService',['$http',function($http) {

    var map = new L.Map("map", {
        'zoomControl': true,
        'scrollWheelZoom': true
    });

    var defaultLocation = new L.LatLng(_default_view.lat,_default_view.lon);
    var defaultZoom = _default_view.zoom;

    map.addLayer(new L.TileLayer(_tiles_url,_tiles_opt));
    map.setView(defaultLocation,defaultZoom);

    var markerLayer = L.layerGroup().addTo(map);
    var icons = {};

        // create icon for old projects
        icons.old = {
            icon: L.icon({
                iconUrl: _static_url + 'img/icons/grau.png',
                iconSize:     [26, 45],
                iconAnchor:   [13, 45],
                popupAnchor:  [0, -46]
            })
        };

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
            map.fitBounds(poly.getBounds(), setViewOptions);
        },

        resetToDefaults: function() {
            map.setView(defaultLocation, defaultZoom,  setViewOptions);
        }
    };
}]);
