var marker;
var map;

function drawMap(){
    // create a form row for the map
    var html = '<div class="form-row">';
    html += '<label>Karte:</label>';
    html += '<div id="adminmap"></div>';
    html += '<p class="help">Bewegen Sie den Marker mit der Maus um den Ort anzupassen</p>';
    html += '</div>';
    $('.field-entities').after(html);

    // add the map layer
    map = new L.Map("adminmap");
    map.addLayer(new L.TileLayer(_tiles_url + '/{z}/{x}/{y}.png',_tiles_opt));

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

    // crate an icon for the marker
    var greyIcon = L.icon({
        iconUrl: '/static/img/icons/gruen.png',
        iconSize:     [26, 45], // size of the icon width,height
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
    });

    // add a marker to the map
    marker = L.marker([lat,lon],{icon: greyIcon, draggable: true}).addTo(map);

    // make the marker draggable
    marker.on('dragend', function(event) {
        var result = event.target.getLatLng();
        $('#id_lat').val(result.lat);
        $('#id_lon').val(result.lng);
    });

    // create a button for automatic coordinate discovery
    var button = $('<p/>', {
        html: '<input type="button" value="Adresse auf Karte markieren" class="btn"></input>'
    })
    .appendTo($('.field-entities'))
    .click(function(){
        // remove old error message
        $('.map-error').remove();

        // get the address from the form field
        var address = $('#id_address').val();
        if (address.length === 0) {
            $('.field-entities').append('<p class="map-error">Bitte geben Sie eine Adresse ein.</p>');
        }

        // get the entities from the form field
        var entities = [];
        $("#id_entities option:selected").each(function () {
            entities.push($(this).text());
        });
        if (entities.length === 0) {
            $('.field-entities').append('<p class="map-error">Bitte geben Sie einen Bezirk an.</p>');
        }

        // query nominatim.openstreetmap.org for the coordinates
        if (address.length !== 0 && entities.length !== 0) {
            var url = 'http://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + address + ' ' + entities.join(' ') + ' ' + 'Berlin';
            $.ajax({
                dataType: "json",
                url: url,
                success: function(data) {
                    if(data.length !== 0){
                        var lon = data[0].lon;
                        var lat = data[0].lat;
                        var location = new L.LatLng(lat, lon);
                        marker.setLatLng(location);
                        map.panTo(location);
                        map.setZoom(16);
                        $('#id_lat').val(lat);
                        $('#id_lon').val(lon);
                    } else {
                        $('.field-entities').append('<p class="map-error">Es wurde kein Eintrag gefunden: Bitte Korrigieren Sie die Rechtschreibung der Adresse oder geben Sie die Geokoordinaten manuell ein.</p>');
                    }
                },
                error: function(jqXHR,textStatus,errorThrown) {
                    $('.field-entities').append('<p class="map-error">Der Service ist gerade nicht erreichbar: Bitte tragen Sie die Geokoordinaten manuell ein oder versuchen Sie es später noch einmal.</p>');
                }
            });
        }
    });
}

$(document).ready(function() {
    setTimeout('drawMap()',100);
});