function initMap() {
    map = new L.Map("localmap");
    
    var min = 14; //minimale Zoomstufe
    var max = 16; //maximale Zoomstufe	
    
    var myTiles = "http://tiles.jochenklar.de/bbs/{z}/{x}/{y}.png";
    var	osmCopyright = ""; //Copyrigth, das unten rechts erscheint	
    var myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } );  
    map.addLayer(myLayer);   
    
    var center = new L.LatLng(lat, lon); 	
    map.setView(center, min);
    
    var icon;
    
    if(typ == "Öffentliche Auslegung"){
        icon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_organge_klein.png',
        iconSize:     [26, 45], // size of the icon width,height                                    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location  
        });
    }
    else if(typ == "Frühzeitige Öffentlichkeitsbeteiligung"){
        icon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_tuerkis_klein.png',
        iconSize:     [26, 45], // size of the icon width,height                                    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location 
        });   
    } 
    
    else{
        icon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_blau_klein.png',
        iconSize:     [26, 45], // size of the icon width,height                                    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location
        });     
    } 
    
    console.log(icon);      
    
        
    L.marker([lat,lon],{icon: icon}).addTo(map);
}

$(document).ready(function() {
    setTimeout('initMap()',100);     
});