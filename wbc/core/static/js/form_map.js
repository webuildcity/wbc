var map;       
    // add the map layer
map = new L.Map("form-map");
map.addLayer(new L.TileLayer(_tiles_url, _tiles_opt));

// get lat and lon from the form fields
var lat, lon;
if($('#id_lat').val() !== '') {
    lat = $('#id_lat').val();
} else {
    lat = _default_view.lat;
}
if($('#id_lon').val() !== '') {
    lon = $('#id_lon').val();
} else {
    lon = _default_view.lon;
}

// center map
map.setView(new L.LatLng(lat,lon),_default_view.zoom);

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

var options = {
    position: 'topright',
    draw: {
        polyline: false,
        polygon: {
            allowIntersection: false, // Restricts shapes to simple polygons
            drawError: {
                color: '#e1e100', // Color the shape will turn when intersects
                message: '<strong>Error!<strong> stick to simple polygons!' // Message that will show when intersect
            },
            shapeOptions: {
                color: '#bada55'
            }
        },
        circle: false, // Turns off this drawing tool
        rectangle: false,
        // marker: {
        //     icon: new MyCustomMarker()
        // }
    },
    edit: {
        featureGroup: drawnItems, //REQUIRED!!
        // remove: false
    }
};

// Initialise the draw control and pass it the FeatureGroup of editable layers
var drawControl = new L.Control.Draw(options);
map.addControl(drawControl);


setTimeout(function() {
    map.invalidateSize();
}, 200);

// if (_polygon){
//     if( _polygon.length > 0 ) {
//         var polygon = L.multiPolygon(_polygon);
//         drawnItems.addLayer(polygon);
//     }
    
// }

map.on('draw:created', function (e) {
    var type = e.layerType,
        layer = e.layer;
    globe = e;
    if (type === 'marker') {
        layer.bindPopup('My Location!');
    }
    if (type === 'polygon') {
        console.log(e.layer.toGeoJSON().geometry.coordinates.toString());
    }

    drawnItems.addLayer(layer);
});