var leafletMap

function displaymap() {
    leafletMap = L.map('map').setView([52.51, 13.37628], 10);

    var base = {
	'osm-bright': L.tileLayer('http://tiles.jochenklar.de/bright/{z}/{x}/{y}.png', {
            attribution: 'Style by <a href="https://github.com/mapbox/osm-bright">OSM-Bright</a>',
            minZoom: 10,
            maxZoom: 15
        }).addTo(leafletMap)
    }

    L.control.layers(base,{}, {
        collapsed: false
    }).addTo(leafletMap);
}

function init() {
    displaymap();
}

$(document).ready(function() {
    setTimeout("init();", 100);
});
