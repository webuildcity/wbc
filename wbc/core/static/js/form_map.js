var map;    
var marker;   


$(document).ready(function(){


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

    // leaflet draw doesnt like grouped layers, so this is the way to go
    function addNonGroupLayers(sourceLayer, targetGroup) {
        if (sourceLayer instanceof L.LayerGroup) {
            sourceLayer.eachLayer(function (layer) {
                addNonGroupLayers(layer, targetGroup);
            });
        } else {
            targetGroup.addLayer(sourceLayer);
        }
    }

    // check if we got a polygon (TODO: only for edit in future pls)
    if (typeof(_polygon)!== 'undefined'){
        if( _polygon.length > 0 ) {
            var polygon = L.multiPolygon(_polygon);
            // drawnItems.addLayer(polygon);
            addNonGroupLayers(polygon, drawnItems)
        }
    }

    // check if we got a polygon (TODO: only for edit in future pls)
    if (typeof(_lat) !== 'undefined'){
        marker = L.marker([_lat, _lon]);
        drawnItems.addLayer(marker); 
    }

    map.on('draw:created', function (e) {
        var type = e.layerType,
            layer = e.layer;
        globe = e;
        drawnItems.addLayer(layer);
        if (type === 'marker') {

            $('#id_lat').val(layer._latlng.lat);
            $('#id_lon').val(layer._latlng.lng);
            drawnItems.removeLayer(layer);
            drawnItems.removeLayer(marker);
            marker = L.marker([layer._latlng.lat, layer._latlng.lng])
            drawnItems.addLayer(marker);
        }
        if (type === 'polygon') {

            var polygonString = '[';

            for (var layer in drawnItems._layers){
                if (drawnItems._layers[layer].editing._poly){

                    if (!drawnItems._layers[layer]._layers){

                        layer =  drawnItems._layers[layer].toGeoJSON();
                        var coordinates = layer.geometry.coordinates.length > 1 ? layer.geometry.coordinates : layer.geometry.coordinates[0];
                        for (coords in coordinates) {
                            //necessary to get the coordinates in the same format as the data from the cities wfs
                            coordinates[coords] = [coordinates[coords][1], coordinates[coords][0]]
                        }
                        polygonString += JSON.stringify(coordinates, null, 2);
                        polygonString += ',';   
                    } else {
                        for (var layer2 in drawnItems._layers[layer]._layers){
                            layer2 =  drawnItems._layers[layer]._layers[layer2].toGeoJSON();

                            var coordinates = layer2.geometry.coordinates.length > 1 ? layer2.geometry.coordinates : layer2.geometry.coordinates[0];
                            for (coords in coordinates) {
                                coordinates[coords] = [coordinates[coords][1], coordinates[coords][0]]
                            }
                            polygonString += JSON.stringify(coordinates, null, 2);
                            polygonString += ',';
                        }
                    }
                }
            }
            polygonString += ']';
            $('#id_polygon').val(polygonString);
        }

    });
});
// var recursiveGeoJsonParse = function(layerContainer){
//     for (var layer in layerContainer){
//         if (drawnItems._layers[layer]._layers){
//             console.log(drawnItems._layers[layer]._layers)
//             layer =  drawnItems._layers[layer].toGeoJSON();
//         } else {
//             recursiveGeoJsonParse(layer);
//         }
//         var coordinates = layer.geometry.coordinates.length > 1 ? layer.geometry.coordinates : layer.geometry.coordinates[0];

//         for (coords in coordinates) {
//             //necessary to get the coordinates in the same format as the data from the cities wfs
//             coordinates[coords] = [coordinates[coords][1], coordinates[coords][0]]

//         }
//         console.log(coordinates);
//         polygonString += JSON.stringify(coordinates, null, 2);
//     }
//     polygonString += ']';
//     $('#id_polygon').val(polygonString);
// };