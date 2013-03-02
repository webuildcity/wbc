function initMap() {
   	
    map = new L.Map("map1");
    
    var min = 11; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	
    var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } );  
    map.addLayer(myLayer);   
    
	var center = new L.LatLng(lat, lon); 	
	map.setView(center, min);	 
    
}

$(document).ready(function() {
    setTimeout('initMap()',100);    
    
});