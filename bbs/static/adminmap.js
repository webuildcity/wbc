var marker;
var map;

function drawMap(){
	var html = '<div class="form-row">';
        html += '<label>Karte:</label>';
	html += '<div id="adminmap"></div>';
	html += '<p class="help">Bewegen Sie den Marker mit der Maus um den Ort anzupassen</p>';
        html += '</div>';

	$('.field-bezirke').after(html);
	map = new L.Map("adminmap");

	var min = 10;
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

    var lan;
    var lon;

	if($('#id_lat').val()!= '') lan = $('#id_lat').val();
	else lan = 52.51;

	if($('#id_lon').val()!= '') lon = $('#id_lon').val();
	else lon = 13.37628;   	
	

	map.addLayer( myLayer );
	var center = new L.LatLng(lan, lon);
	map.setView(center, min);


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

	var button = $('<p/>', {
		html: '<input type="button" value="Adresse auf Karte markieren" class="btn"></input>'
	})
	.appendTo($('.field-bezirke'))
	.click(function(){
		$('div').remove('.alert.alert-error');		
		var adresse;
		var bezirk;
		if ($('#id_adresse','#projekt_form', '#content').val()){
			$('div.tab-content.tab-content-main').remove('div.alert.alert-error')
			adresse = $('#id_adresse','#projekt_form', '#content').val();
			if ($('#id_bezirke','#projekt_form', '#content').find(":selected").length != 0){
				$('#feedback').text('');
				bezirk = $('#id_bezirke','#projekt_form', '#content').find(":selected")[0].text;
			}
			else $('div.tab-content.tab-content-main').prepend('<div class="alert alert-error">Bitte geben Sie einen Bezirk ein</div>');
		}  
		else $('div.tab-content.tab-content-main').prepend('<div class="alert alert-error">Bitte geben Sie eine Adresse ein</div>')

		 
		
		if (adresse && bezirk) {
			var url = 'http://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + adresse + ' ' + bezirk + ' ' + 'Berlin';
			$.ajax({  	
				dataType: "json",  
				url: url,
				success: function(data) {
					if(data.length != 0){
						var lon = data[0].lon;
						var lat = data[0].lat;
						var location = new L.LatLng(lat, lon);
						marker.setLatLng(location); 
						map.panTo(location);
						map.setZoom(16);
						$('#id_lat').val(lat);
		    			$('#id_lon').val(lon);
					}
					else $('div.tab-content.tab-content-main').prepend('<div class="alert alert-error">Es wurde kein Eintrag gefunden: Bitte Korrigieren Sie die Rechtschreibung der Adresse oder geben Sie den Ort manuell ein</div>');
					
					
		    	},
		    	error: function(jqXHR,textStatus,errorThrown) {
		    		$('div.tab-content.tab-content-main').prepend('<div class="alert alert-error">Der Service ist gerade nicht erreichbar: Bitte tragen Sie die Geokoordinaten manuell ein oder versuchen Sie es später noch einmal</div>');
      				
    			}
			});
		}
	});
}


$(document).ready(function() {
    setTimeout('drawMap()',100);
});