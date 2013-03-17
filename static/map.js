var markers = new Array();

function initMap() {
	// Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 10; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	
        osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
	var center = new L.LatLng(52.51, 13.37628); //Fokus der Karte	
	map.setView(center, 11);		
	
	var orangeIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_organge_klein.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	});
    var markedIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/groß/schild_organge_groß.png',    
        iconSize:     [35, 65], // size of the icon width,height    
        iconAnchor:   [17, 65], // point of the icon which will correspond to marker's location       
	});

    // bbps zu karte hinzufügen
    $.each(bbps, function(key,bbp){
        var text = bbp.fields.address; 
        var bezirk = bbp.fields.bezirk;
        var typid = bbp.fields.typ;        
        var typ = typen[typid-1].fields.name;
        var end = bbp.fields.end;
        var link = siteUrl + "bbp/" + bbp.pk ;

        // marker für leaflet karte
        var marker = L.marker(
            [bbp.fields.lat,bbp.fields.lon],
            {icon: orangeIcon}
        ).addTo(map);

        marker.pk = bbp.pk;

        marker.on('mouseover', function(evt) {
            $('a', '#bbp-' + this.pk).addClass("marked");
            //markers[this.pk].setIcon(markedIcon);
        });
        marker.on('mouseout', function(evt) {
            $('a', '#bbp-' + this.pk).removeClass("marked");
            //markers[this.pk].setIcon(orangeIcon);
        });

        var popuptext = typ;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + end;
        popuptext += '<br>';
        popuptext += '<a href="' + link + '" target="blank">Details</a>';
        marker.bindPopup(popuptext);

        // add marker to global marker array
        markers[bbp.pk] = marker;

        // listeneintrag für sidebar
        var li = $('<li/>',{
            'id': 'bbp-'+ bbp.pk,
            'html': '<a href="' + link + '" target="blank">Betrifft die Gegend um: ' + '<b>' +text + '</b> in ' + bezirke[bezirk-1].fields.name +'</a>'
        }).appendTo($('ul', '#sidebar-content'));

        // mouseover effekte für listeneintrag
        li.mouseover(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).addClass("marked");
            markers[pk].setIcon(markedIcon);
        });
        li.mouseout(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).removeClass("marked");
            markers[pk].setIcon(orangeIcon);
        });
    }); 
    
    var greyIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_grau_klein.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	});
    var markedGreyIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/groß/schild_grau_groß.png',    
        iconSize:     [35, 65], // size of the icon width,height    
        iconAnchor:   [17, 65], // point of the icon which will correspond to marker's location       
	});
    
    $.each(bbpsOld, function(key,bbp){
        var text = bbp.fields.address; 
        var bezirk = bbp.fields.bezirk;
        var typid = bbp.fields.typ;        
        var typ = typen[typid-1].fields.name;
        var end = bbp.fields.end;
        var link = siteUrl + "bbp/" + bbp.pk ;

        // marker für leaflet karte
        var marker = L.marker(
            [bbp.fields.lat,bbp.fields.lon],
            {icon: greyIcon}
        ).addTo(map);

        marker.pk = bbp.pk;

        marker.on('mouseover', function(evt) {
            $('a', '#bbp-' + this.pk).addClass("marked");
            //markers[this.pk].setIcon(markedIcon);
        });
        marker.on('mouseout', function(evt) {
            $('a', '#bbp-' + this.pk).removeClass("marked");
            //markers[this.pk].setIcon(orangeIcon);
        });

        var popuptext = typ;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + end;
        popuptext += '<br>';
        popuptext += '<a href="' + link + '" target="blank">Details</a>';
        marker.bindPopup(popuptext);

        // add marker to global marker array
        markers[bbp.pk] = marker;

        // listeneintrag für sidebar
        var li = $('<li/>',{
            'id': 'bbp-'+ bbp.pk,
            'html': '<a href="' + link + '" target="blank">Betrifft die Gegend um: ' + '<b>' +text + '</b> in ' + bezirke[bezirk-1].fields.name +'</a>'
        }).appendTo($('ul', '#sidebar-content'));

        // mouseover effekte für listeneintrag
        li.mouseover(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).addClass("marked");
            markers[pk].setIcon(markedGreyIcon);
        });
        li.mouseout(function() {
            var pk = $(this).attr('id').split('bbp-')[1];
            $('a', this).removeClass("marked");
            markers[pk].setIcon(greyIcon);
        });
    });
    
    
      
    
    // button für sidebar zur leafletkarte hinzufügen
    html = '<div class="leaflet-control-zoom leaflet-control"><a class="leaflet-control-sidebar" href="#" title="Sidebar anzeigen" id="sidebar-button"><i class="icon-chevron-right"></i></a></div>';
    $('.leaflet-top.leaflet-left').prepend(html);
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