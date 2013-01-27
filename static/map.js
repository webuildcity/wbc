$(document).ready(function() {
	
	
	//Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 11; //minimale Zoomstufe
	var max = 16; //maximale Zoomstufe	
	

	
	myTiles = "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"; //hier wird angegeben von wo die Tiles für die Karte geladen werden sollen
	osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
	var center = new L.LatLng(52.484766470498954, 13.363323211669922); //Fokus der Karte	
	map.setView(center, min);	
	
	var fernsehturm = L.icon({
    iconUrl: '/static/img/Fernsehturm_grau_26px3.png',    
    iconSize:     [27, 125], // size of the icon   
    iconAnchor:   [8,111] // point of the icon which will correspond to marker's location       
	});
	
	var fernsehturmMarker = L.marker([52.520841,13.409405],{icon: fernsehturm}).addTo(map);
	
	
	var funkturm = L.icon({
    iconUrl: '/static/img/Funkturm_36px_neu.png',    
    iconSize:     [36, 110], // size of the icon   
    iconAnchor:   [16,108] // point of the icon which will correspond to marker's location       
	});	
	var funkturmMarker = L.marker([52.5050681,13.278211400000032],{icon: funkturm}).addTo(map);
	
	var greenIcon = L.icon({
    iconUrl: '/static/img/marker_green.png',    
    iconSize:     [21, 32], // size of the icon width,height    
    iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
    popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});	
	
	
	var StrassenbauMarker = new Array();
	var StrassenbauLayer = L.layerGroup(StrassenbauMarker).addTo(map);

	//hier wird die KML per Ajax eingelesen
	/*$.get("strassenbau.kml", function(marks){
		
		  $(marks).find("Placemark").each(function(){
			var $m = $(this);
			var koordinaten = $m.find("coordinates").text();
		  	var k = koordinaten.split(",");
		  	var lon = parseFloat(k[0]);
		  	var lat = parseFloat(k[1]);			
		  	var icon = greenIcon;
			
			var name = $m.find("name").text();
			
			var marker = L.marker([lat,lon],{icon: icon});
			marker.bindPopup('<b>'+ name + '</b>');	    
		 	StrassenbauLayer.addLayer(marker);	
		  });	 
		  	  
		  });*/
	  });