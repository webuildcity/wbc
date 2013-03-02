function initMap() {
   	
    map = new L.Map("map1");
    
    var baseurl = '/bbs/static/';
    var min = 14; //minimale Zoomstufe
	var max = 16; //maximale Zoomstufe	
	
    var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	osmCopyright = ""; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } );  
    map.addLayer(myLayer);   
    
	var center = new L.LatLng(lat, lon); 	
	map.setView(center, min);
    
    var greenIcon = L.icon({
        iconUrl: baseurl + '/img/marker_green.png',    
        iconSize:     [21, 32], // size of the icon width,height    
        iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});
    
    L.marker([lat,lon],{icon: greenIcon}).addTo(map);
    	 
    
}

$(document).ready(function() {
    setTimeout('initMap()',100);    
    
});