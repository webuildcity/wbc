function initMap() {
    // add the map layer
    map = new L.Map("localmap");
    var min = 14;
    var max = 17;
    var myLayer = new L.TileLayer('http://tiles.buergerbautstadt.de/berlin/{z}/{x}/{y}.png', {
        minZoom: min,
        maxZoom: max,
        attribution: 'Map data &copy; 2012 OpenStreetMap contributors',
        zIndex: 0,
        errorTileUrl: 'http://tiles.buergerbautstadt.de/error.png',
        reuseTiles: true
    });
    map.addLayer(myLayer);

    // center map
    var center = new L.LatLng(lat, lon); 	
    map.setView(center, 15);
    
    var icon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_gruen_klein.png',
        iconSize:     [26, 45], // size of the icon width,height                                    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location  
    });
    
    var polygonOptions = {
        weight: 3,
        color: '#de6a00',
        opacity: 1,
        fill: false,
        fillColor: '#646464',
        fillOpacity: 0.5
    }

    if (typeof(polygon) !== 'undefined') {
        if (polygontype === 'Polygon') {
            L.polygon(polygon).setStyle(polygonOptions).addTo(map);
        } else if (polygontype === 'MultiPolygon') {
            L.multiPolygon(polygon).setStyle(polygonOptions).addTo(map);
        }
    }
    L.marker([lat,lon],{icon: icon}).addTo(map);

}

$(document).ready(function() {
    setTimeout('initMap()',100);     
});