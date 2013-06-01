var marker;
var map;

function drawMap(){

	
	var html = '<div class = "control-group form-row map"><div>';
	html += '<div class="control-label">Karte</div>';
	html += '<div class="controls"><div id="admin_map"></div>';
	html += '<span class="help-inline">Bewegen Sie den Marker mit der Maus um den Ort anzupassen</span></div></div></div>'

	$('div.control-group.form-row.field-bezirke').after(html);

	map = new L.Map("admin_map");

	var min = 11;
	var max = 17;
    var errorTile = "http://tiles.jochenklar.de/bbs/11/1102/671.png";
	var myTiles = "http://tiles.jochenklar.de/bbs/{z}/{x}/{y}.png";
    var osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors";

	var myLayer = new L.TileLayer(myTiles, {
        minZoom:min,
        maxZoom: max,
        attribution: osmCopyright,
        zIndex:0,
        errorTileUrl: errorTile,
        reuseTiles:true
    });

    var lan = $('#id_lat').val();
	var lon = $('#id_lon').val();

	map.addLayer( myLayer );
	var center = new L.LatLng(lan, lon);
	map.setView(center, 11);


	var greyIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_grau.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	}); 

	

	marker = L.marker([lan,lon],{icon: greyIcon, draggable:true}).addTo(map); 

	marker.on('dragend', function(event) {
    var marker = event.target;  // you could also simply access the marker through the closure
    var result = marker.getLatLng();  // but using the passed event is cleaner
    
    $('#id_lat').val(result.lat);
    $('#id_lon').val(result.lng);
	});

	var button = $('<div/>', {
		html: '<input type="button" value="Adresse auf Karte markieren" class="btn"></input>'
	})
	.appendTo($('div.control-group.form-row.field-bezirke .controls'))
	.click(function(){
		var adresse = $('#id_adresse','#projekt_form', '#content').val();
		var bezirke = $('#id_bezirke','#projekt_form', '#content').find(":selected");
		$.getJSON('http://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + adresse + " " + "Berlin", function(data) {
			var lon = data[0].lon;
			var lat = data[0].lat;
			var location = new L.LatLng(lat, lon);
			marker.setLatLng(location); 
			map.panTo(location);
			$('#id_lat').val(lat);
    		$('#id_lon').val(lon);

		});
		
	});




}


$(document).ready(function() {
    setTimeout('drawMap()',100);
});