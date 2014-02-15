function initMap() {
    // add the map layer
    map = new L.Map("localmap");
    var min = 14;
    var max = 17;
    var myLayer = new L.TileLayer('http://tiles.jochenklar.de/bbs/{z}/{x}/{y}.png', {
        minZoom: min,
        maxZoom: max,
        attribution: 'Map data &copy; 2012 OpenStreetMap contributors',
        zIndex: 0,
        errorTileUrl: 'http://tiles.jochenklar.de/bbs/error.png',
        reuseTiles: true
    });
    map.addLayer(myLayer);

    // center map
    var center = new L.LatLng(lat, lon); 	
    map.setView(center, max);
    
    var icon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_gruen_klein.png',
        iconSize:     [26, 45], // size of the icon width,height                                    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location  
    });
    
    L.marker([lat,lon],{icon: icon}).addTo(map);
}

$(document).ready(function() {
    setTimeout('initMap()',100);     
});