var markers = new Array();

function initMap() {
	// Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 11; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	
    osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
	var center = new L.LatLng(52.51, 13.37628); //Fokus der Karte	
	map.setView(center, 11);
    
    
    //------------------------------------------------Erster Layer: öffentliche Auslegung ------------------------------------------------		
	
	var orangeIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_organge_klein.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	});    
        
    var bbpMarker = new Array();
	var bbpLayer = L.layerGroup(bbpMarker).addTo(map);

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
        );       
        

        marker.pk = bbp.pk;

        marker.on("mouseover", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_grau_klein.png';
        }).on("mouseout", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_organge_klein.png';
        });       
        

        var popuptext = typ;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + end;
        popuptext += '<br>';
        popuptext += '<a href="' + link + '" >Details</a>';        
        marker.bindPopup(popuptext);   
       

        // add marker to global marker array
        markers[bbp.pk] = marker;
        
        bbpLayer.addLayer(marker);
        
    }); 
    
    //------------------------------------------------Zweiter Layer: frühzeitige Öffentlichkeitsbeteiligung------------------------------------------------
    
    var tuerkisIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_tuerkis_klein.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	});   
    
    var bbpFruehMarker = new Array();
	var bbpFruehLayer = L.layerGroup(bbpFruehLayer).addTo(map);
    
    
    $.each(bbpFruehJson, function(key,bbp){
        var text = bbp.fields.address; 
        var bezirk = bbp.fields.bezirk;
        var typid = bbp.fields.typ;        
        var typ = typen[typid-1].fields.name;
        var end = bbp.fields.end;
        var link = siteUrl + "bbp/" + bbp.pk ;

        // marker für leaflet karte
        var marker = L.marker(
            [bbp.fields.lat,bbp.fields.lon],
            {icon: tuerkisIcon}
        ).addTo(map);        
        
        bbpFruehLayer.addLayer(marker)

        marker.pk = bbp.pk;
        
        var popuptext = typ;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + end;
        popuptext += '<br>';
        popuptext += '<a href="' + link + '" >Details</a>';
        marker.bindPopup(popuptext);        
        
        marker.on("mouseover", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_grau_klein.png';
        }).on("mouseout", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_tuerkis_klein.png';
        });       
        

        // add marker to global marker array
        markers[bbp.pk] = marker;

        
    }); 
    
    
    //------------------------------------------------Dritter Layer: erneute Öffentlichkeitsbeteiligung------------------------------------------------
    
    var blauIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_blau_klein.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
	});   
    
    var bbpErneutMarker = new Array();
	var bbpErneutLayer = L.layerGroup(bbpErneutLayer).addTo(map);
    
    
    $.each(bbpErneutJson, function(key,bbp){
        var text = bbp.fields.address; 
        var bezirk = bbp.fields.bezirk;
        var typid = bbp.fields.typ;        
        var typ = typen[typid-1].fields.name;
        var end = bbp.fields.end;
        var link = siteUrl + "bbp/" + bbp.pk ;

        // marker für leaflet karte
        var marker = L.marker(
            [bbp.fields.lat,bbp.fields.lon],
            {icon: blauIcon}
        ).addTo(map);        
        
        bbpErneutLayer.addLayer(marker)

        marker.pk = bbp.pk;
        
        var popuptext = typ;
        popuptext += '<br>';
        popuptext += "Beteiligung möglich bis: " + end;
        popuptext += '<br>';
        popuptext += '<a href="' + link + '" >Details</a>';
        marker.bindPopup(popuptext);        
        
        marker.on("mouseover", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_grau_klein.png';
        }).on("mouseout", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_blau_klein.png';
        });       
        

        // add marker to global marker array
        markers[bbp.pk] = marker;

        
    }); 
      
    
    $('input[name=aktuell]').click(function(){
        if(this.checked) {
            map.addLayer(bbpLayer);            
        } 
        
        else { 
        map.removeLayer(bbpLayer);         
        }
        
    });
    
    $('input[name=frueh]').click(function(){
        if(this.checked) {
            map.addLayer(bbpFruehLayer);            
        }
        
        else {
            map.removeLayer(bbpFruehLayer); 
            
        }
        
    });  
    
    $('input[name=erneut]').click(function(){
        if(this.checked) {
            map.addLayer(bbpErneutLayer);            
        }
        
        else {
            map.removeLayer(bbpErneutLayer); 
            
        }
        
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
});ue