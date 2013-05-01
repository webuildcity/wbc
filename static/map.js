var layers = {};

function initMap() {
	var map = new L.Map("map");
    console.log(verfahrensschritte);
	var min = 11;
	var max = 17;
	var myTiles = "http://tiles.jochenklar.de/bbs/{z}/{x}/{y}.png";
    var osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors";

	var myLayer = new L.TileLayer(myTiles, {
        minZoom:min,
        maxZoom: max,
        attribution: osmCopyright,
        zIndex:0,
        reuseTiles:true
    });

	map.addLayer( myLayer );
	var center = new L.LatLng(52.51, 13.37628);
	map.setView(center, 11);
    
    $.each(verfahrensschritte, function(key, vs) {
        var layer = {}

        layer.iconUrl = staticUrl + vs.icon;

        layer.icon = L.icon({
            iconUrl: staticUrl + vs.icon,
            iconSize:     [26, 45], // size of the icon width,height    
            iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
            popupAnchor:  [0, -46]  // point from which the popup should open relative to the iconAnchor
        });

        layer.layerGroup = L.layerGroup().addTo(map);

        layers[vs.pk] = layer;
        
        $('input[name=vs-'+vs.pk+']').click(function(){
            if(this.checked) {
                map.addLayer(layers[vs.pk].layerGroup);            
            } else { 
                map.removeLayer(layers[vs.pk].layerGroup);         
            }
        });
    });
    console.log(points);
    // bbps zu karte hinzufügen
    $.each(points, function(key, point){
        var marker = L.marker(
            [point.lat,point.lon],
            {icon: layers[point.vspk].icon}
        ); 

        marker.oldIcon = layers[point.vspk].iconUrl;

        marker.on("mouseover", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_gruen_klein.png';
        }).on("mouseout", function(e) {
            e.target._icon.src = this.oldIcon;
        });

        var popuptext = '<a href="/info" >' + verfahrensschritte[point.vspk].name + '</a>';
        popuptext += '<br>';
        popuptext += "Betrifft Gegend um: " + point.adresse;
        popuptext += '<br>';
        popuptext += "Verantwortlich: " + point.behoerde;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + point.ende;
        popuptext += '<br>';
        popuptext += '<a href="' + siteUrl + "projekte/" + point.projekt + '" >Details</a>';        
        marker.bindPopup(popuptext);
        marker.addTo(map);

        layers[point.vspk].layerGroup.addLayer(marker);
    }); 

    // button für sidebar zur leafletkarte hinzufügen
    html = '<div class="leaflet-control-zoom leaflet-control"><a class="leaflet-control-sidebar" href="#" id="sidebar-button"><i class="icon-chevron-left"></i></a></div>';
    $('.leaflet-top.leaflet-left').prepend(html);
    $('#sidebar-button').click(moveOutSidebar);
    $('#sidebar-button').attr('title','Sidebar ausblenden');
    $('.leaflet-control-zoom-in').attr('title','Hinein zoomen');
    $('.leaflet-control-zoom-out').attr('title','Heraus zoomen');
}

function moveOutSidebar(){
    $('#sidebar-button').unbind('click');
    $('#sidebar').animate(
        {left: '-=310'},
        'fast',
        function(){});
    $('.leaflet-top.leaflet-left').animate(
        {left: '-=310'},
        'fast',
        function(){
            $('#sidebar-button').click(moveInSidebar);
            $('i', '#sidebar-button').remove();
            $('#sidebar-button').append('<i class="icon-chevron-right"></i>');
	    $('#sidebar-button').attr('title','Sidebar einblenden');
       }
    );
    return false;
}

function moveInSidebar(){
    $('#sidebar-button').unbind('click');
    $('#sidebar').animate(
        {left: '+=310'},
        'fast',
        function(){});
    $('.leaflet-top.leaflet-left').animate(
        {left: '+=310'},
        'fast',
        function(){
            $('#sidebar-button').click(moveOutSidebar);
            $('i', '#sidebar-button').remove();
            $('#sidebar-button').append('<i class="icon-chevron-left"></i>');
	    $('#sidebar-button').attr('title','Sidebar einblenden');
        }
    );
    return false;
}

$(document).ready(function() {
    setTimeout('initMap()',100);
});