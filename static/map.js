var _markers = new Array();

function initMap() {
	// Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 10; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	
    var baseurl = '/bbs/static/';
    var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
	var center = new L.LatLng(52.51, 13.37628); //Fokus der Karte	
	map.setView(center, 11);		
	
	var orangeIcon = L.icon({
        iconUrl: baseurl + '/img/schild_orange.png',    
        iconSize:     [23, 37], // size of the icon width,height    
        iconAnchor:   [11, 37], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0,-37] // point from which the popup should open relative to the iconAnchor
	});
    var markedIcon = L.icon({
        iconUrl: baseurl + '/img/marker_yellow.png',    
        iconSize:     [21, 32], // size of the icon width,height    
        iconAnchor:   [10, 32], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0,-32] // point from which the popup should open relative to the iconAnchor
	});

    // bbps zu karte hinzufügen
    $.each(bbps, function(key,bbp){
        var text = bbp.fields.bplan;
        var link = site_url + "bbp/" + bbp.pk ;

        // marker für leaflet karte
        var marker = L.marker(
            [bbp.fields.lat,bbp.fields.lon],
            {icon: orangeIcon}
        ).addTo(map);

        marker.pk = bbp.pk;

        marker.on('mouseover', function(evt) {
            $('a', '#bbp-' + this.pk).addClass("marked");
            //_markers[this.pk].setIcon(markedIcon);
        });
        marker.on('mouseout', function(evt) {
            $('a', '#bbp-' + this.pk).removeClass("marked");
            //_markers[this.pk].setIcon(orangeIcon);
        });

        var popuptext = text;
        popuptext += '<br>';
        popuptext += '<a href=' + link + '" target="blank">Details</a>';
        marker.bindPopup(popuptext);

        // add marker to global marker array
        _markers[bbp.pk] = marker;

        // listeneintrag für sidebar
        var li = $('<li/>',{
            'id': 'bbp-'+ bbp.pk,
            'html': '<a href="' + link + '" target="blank">' + text + '</a>'
        }).appendTo($('ul', '#sidebar-content'));

        // mouseover effekte für listeneintrag
        li.mouseover(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).addClass("marked");
            _markers[pk].setIcon(markedIcon);
        });
        li.mouseout(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).removeClass("marked");
            _markers[pk].setIcon(orangeIcon);
        });
    });   
    
    // button für sidebar zur leafletkarte hinzufügen
    html = '<div class="leaflet-control-zoom leaflet-control"><a class="leaflet-control-sidebar" href="#" title="Sidebar anzeigen" id="sidebar-button"><i class="icon-chevron-right"></i></a></div>';
    $('.leaflet-top.leaflet-left').append(html);
    $('#sidebar-button').click(moveInSidebar);
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
        }
    );
    return false;
}

$(document).ready(function() {
    setTimeout('initMap()',100);
});