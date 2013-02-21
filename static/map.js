function initMap() {
	//Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 11; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	
        var baseurl = '/bbs/static/'
        var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
    
    //52.484766470498954, 13.363323211669922
	var center = new L.LatLng(52.51, 13.37628); //Fokus der Karte	
	map.setView(center, min);	
	
	var fernsehturm = L.icon({
        iconUrl: baseurl + '/img/Fernsehturm_grau_26px3.png',    
        iconSize:     [27, 125], // size of the icon   
        iconAnchor:   [8,111] // point of the icon which will correspond to marker's location       
	});
	
	var fernsehturmMarker = L.marker([52.520841,13.409405],{icon: fernsehturm}).addTo(map);
	
	
	var funkturm = L.icon({
        iconUrl: baseurl + '/img/Funkturm_36px_neu.png',    
        iconSize:     [36, 110], // size of the icon   
        iconAnchor:   [16,108] // point of the icon which will correspond to marker's location       
	});	
	var funkturmMarker = L.marker([52.5050681,13.278211400000032],{icon: funkturm}).addTo(map);
	
	var greenIcon = L.icon({
        iconUrl: baseurl + '/img/marker_green.png',    
        iconSize:     [21, 32], // size of the icon width,height    
        iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});	    
    
    var redIcon = L.icon({
        iconUrl: baseurl + '/img/marker_red.png',    
        iconSize:     [21, 32], // size of the icon width,height    
        iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});
    
    var i = 0;
	
	var html = '<ul class="nav nav-pills nav-stacked">';
    
    $.each(bbps, function(key,bbp){
        var lon = bbp.fields.lon;
        var lat = bbp.fields.lat;
        var t = bbp.fields.vorhaben;
        var link = bbp.fields.link;
        var id = "listid" + i;
        console.log(id);
        html += '<li id= "'+ id +'"><a href="' + link + '" target="blank">' + t + '</a></li>';        
        var marker = L.marker([lat,lon],{icon: redIcon}).addTo(map);
        marker.listid = id;                        
        popuptext = "<a href=" + '"' + link + '"' + 'target="blank">' + t + "</a>";
        marker.on('mouseover', function(evt) {
            $('#' + this.listid).addClass("marked");                 
            
        });
        marker.on('mouseout', function(evt) {
            $('#' + this.listid).removeClass("marked");              
            
        });
        marker.bindPopup(popuptext);       
        i++;
    });
    
    
    $.each(projects, function(key,project){
        var lon = project.fields.lon;
        var lat = project.fields.lat;
        var t = project.fields.titel;
        var id2 = "listid" + i;
        html += '<li id= "'+ id2 +'" ><a href="' + project.fields.link + '" target="blank">' + t + '</a></li>';
        var marker = L.marker([lat,lon],{icon: greenIcon}).addTo(map);
        marker.listid = id2;
        marker.on('mouseover', function(evt) {
            $('#' + this.listid).addClass("marked");                 
            
        });
        marker.on('mouseout', function(evt) {
            $('#' + this.listid).removeClass("marked");              
            
        }); 
        marker.bindPopup(t); 
        i++;      
    });
    html += '</ul>';
    $('#sidebar-content').append(html);
    
}

function moveOutSidebar(){
    $('#sidebar-button').unbind('click');
    $('#sidebar').removeClass('sidebar-shadow');
    $('#sidebar').animate(
        {left: '-=300'},
        'fast',
        function(){});
    $('#sidebar-button').animate(
        {left: '-=300'},
        'fast',
        function(){
            $('#sidebar-button').click(moveInSidebar);
            $('i', '#sidebar-button').remove();
            $('#sidebar-button').append('<i class="icon-chevron-right"></i>');
	    $('#sidebar').removeClass('sidebar-shadow');
        }
    );
}

function moveInSidebar(){
    $('#sidebar-button').unbind('click');
    $('#sidebar').addClass('sidebar-shadow');
    $('#sidebar').animate(
        {left: '+=300'},
        'fast',
        function(){});
    $('#sidebar-button').animate(
        {left: '+=300'},
        'fast',
        function(){
            $('#sidebar-button').click(moveOutSidebar);
            $('i', '#sidebar-button').remove();
            $('#sidebar-button').append('<i class="icon-chevron-left"></i>');
        }
    );
}

$(document).ready(function() {
    setTimeout('initMap()',100);    
    $('#sidebar-button').click(moveInSidebar);
});