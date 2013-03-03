var markers = new Array();

function initMap() {
	//Die Karte wird in der index-html in das Div mit der id "mymap" gezeichnet
	map = new L.Map("map");
	
	var min = 10; //minimale Zoomstufe
	var max = 15; //maximale Zoomstufe	
	
    var baseurl = '/bbs/static/';
    var myTiles = "http://tiles.jochenklar.de/pinkoding-bbs/{z}/{x}/{y}.png";
	osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors"; //Copyrigth, das unten rechts erscheint	
	myLayer = new L.TileLayer(myTiles, { minZoom:min, maxZoom: max, attribution: osmCopyright, zIndex:0, reuseTiles:true } ); //Nun wird mit diesen tiles eine ebene erstellt (hier gibt es nur eine Ebene, es sind aber auch mehrere Ebenen möglich)	
	map.addLayer( myLayer ); //Füge die Ebene der Karte hinzu			
	
    
    //52.484766470498954, 13.363323211669922
	var center = new L.LatLng(52.51, 13.37628); //Fokus der Karte	
	map.setView(center, 11);		
	
	var orangeIcon = L.icon({
        iconUrl: baseurl + '/img/schild_orange.png',    
        iconSize:     [25, 35], // size of the icon width,height    
        iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});	  
    
    
    var markedIcon = L.icon({
        iconUrl: baseurl + '/img/marker_yellow.png',    
        iconSize:     [21, 32], // size of the icon width,height    
        iconAnchor:   [14, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [4, -20] // point from which the popup should open relative to the iconAnchor
	});
    
    var i = 1;
	
	var html = '<ul id="list" class="nav nav-pills nav-stacked">';
    //var html = '<ul id="list">';
    
    $.each(bbps, function(key,bbp){
        var lon = bbp.fields.lon;
        var lat = bbp.fields.lat;
        var t = bbp.fields.bplan;
        var link = "http://localhost:8000/bbs/" + bbp.pk ;
        var id = "listid" + bbp.pk ;        
        html += '<li id= "'+ id +'"><a href="' + link + '" target="blank">' + t + '</a></li>';        
        var marker = L.marker([lat,lon],{icon: orangeIcon}).addTo(map);
        marker.listid = id; 
        markers[i] = marker;                       
        popuptext = t + "<br><a href=" + '"' + link + '"' + 'target="blank">' + "Details" + "</a>";
        marker.on('mouseover', function(evt) {
            $('#' + this.listid).addClass("marked");                 
            
        });
        marker.on('mouseout', function(evt) {
            $('#' + this.listid).removeClass("marked");              
            
        });
        marker.bindPopup(popuptext);       
        i++;
    });   
    
    html += '</ul>';
    $('#sidebar-content').append(html); 
     
         
    for(var j = 0; j<markers.length;j++){     
        $('#listid' + j).mouseover(function() {
            k = $(this).attr('id').split('listid')[1];
            $(this).addClass("marked");
            markers[k].setIcon(markedIcon);
        });
        $('#listid' + j).mouseout(function() {
            k = $(this).attr('id').split('listid')[1];
            $(this).removeClass("marked");
            markers[k].setIcon(orangeIcon);
        });
    }
    
    
    
}

function moveOutSidebar(){
    $('#sidebar-button').unbind('click');
    $('#sidebar').removeClass('sidebar-shadow');
    $('#sidebar').animate(
        {left: '-=310'},
        'fast',
        function(){});
    $('#sidebar-button').animate(
        {left: '-=310'},
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
        {left: '+=310'},
        'fast',
        function(){});
    $('#sidebar-button').animate(
        {left: '+=310'},
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