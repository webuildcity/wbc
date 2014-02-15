var layers = {};

function init() {
    initMap();
}

function initMap() {   
    var map = new L.Map("map");

    var min = 9;
    var max = 17;
    var errorTile = "http://tiles.jochenklar.de/bbs/11/1102/671.png";
    var myTiles = "http://tiles.jochenklar.de/bbs/{z}/{x}/{y}.png";
    var osmCopyright = "Map data &copy; 2012 OpenStreetMap contributors";

    var myLayer = new L.TileLayer(myTiles, {
        minZoom:min,
        maxZoom: max,
        attribution: osmCopyright,
        zIndex:0,
        errorTileUrl: errorTile,
        reuseTiles:true
    });

    map.addLayer( myLayer );
    var center = new L.LatLng(52.51, 13.37628);
    map.setView(center, 11);
    
    $.each(verfahrensschritte, function(key, vs) {
        var layer = {}

        layer.iconUrl = staticUrl + vs.icon;
        layer.hoverIconUrl = staticUrl + vs.hoverIcon;

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

    // projekte zu karte hinzufügen
    $.each(points, function(key, point){
        var marker = L.marker(
            [point.lat,point.lon],
            {icon: layers[point.vspk].icon}
        ); 

        marker.icon = layers[point.vspk].iconUrl;
        marker.hoverIcon = layers[point.vspk].hoverIconUrl;

        marker.on("mouseover", function(e) {
            e.target._icon.src = this.hoverIcon;
        }).on("mouseout", function(e) {
            e.target._icon.src = this.icon;
        });

        var popuptext = '<p><b>' + verfahren[point.vpk].name + '</b>';
        popuptext += '<p><i>' + verfahrensschritte[point.vspk].name + '</i>';
        popuptext += ' <a href="/begriffe/#'+ point.vspk + '" >(?)</a></p>';
        popuptext += '<p>Betrifft Gegend um: ' + point.adresse + '</p>';
        popuptext += '<p>Verantwortlich: ' + point.behoerde + '</p>';
        popuptext += '<p>Beteiligung möglich bis: ' + point.ende + '</p>';
        popuptext += '<p><a href="' + siteUrl + "orte/" + point.projekt + '" >Details</a></p>';

        marker.bindPopup(popuptext, {autoPanPaddingTopLeft: new L.Point(10,100), autoPanPaddingBottomRight: new L.Point(10,0)});
        marker.addTo(map);

        layers[point.vspk].layerGroup.addLayer(marker);
    }); 
    
    var greyIcon = L.icon({
        iconUrl: staticUrl + '/img/Baustellenschilder/klein/schild_grau_blass.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
    });   
    
    var oldMarker = new Array();
    var oldLayer = L.layerGroup(oldLayer);
    
    $.each(pointsOld, function(key,point){
        
        // marker für leaflet karte
        var marker = L.marker(
            [point.lat,point.lon],
            {icon: greyIcon}
        );        
        
        oldLayer.addLayer(marker)

        marker.pk = point.pk;
        
        var popuptext = '<p><b>' + verfahren[point.vpk].name + '</b>';
        popuptext += '<p><i>' + verfahrensschritte[point.vspk].name + '</i>';
        popuptext += ' <a href="/begriffe/#'+ point.vspk + '" >(?)</a></p>';
        popuptext += '<p>Betrifft Gegend um: ' + point.adresse + '</p>';
        popuptext += '<p>Verantwortlich: ' + point.behoerde + '</p>';
        popuptext += '<p>Beteiligung war möglich bis: ' + point.ende + '</p>';
        popuptext += '<p><a href="' + siteUrl + "orte/" + point.projekt + '" >Details</a></p>';
        
        marker.bindPopup(popuptext, {autoPanPaddingTopLeft: new L.Point(10,100), autoPanPaddingBottomRight: new L.Point(10,0)});        
        
        marker.on("mouseover", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_grau.png';
        }).on("mouseout", function(e) {
            e.target._icon.src = staticUrl + '/img/Baustellenschilder/klein/schild_grau_blass.png';
        }); 
    
     });   
    
    $('input[name=old]').click(function(){
        if(this.checked) {
            map.addLayer(oldLayer);            
        } else { 
            map.removeLayer(oldLayer);         
        }
    });
    
    var zoom = $('.leaflet-control-zoom').remove();
    zoom.appendTo($('#buttons-left'));
    $('.leaflet-control-attribution').remove();

    $('<div />', {
        'class': 'leaflet-control-zoom leaflet-bar leaflet-control pull-left',
        'html': '<a class="info-button leaflet-control-zoom-out" href="#" title="Info">i</a>'
    }).appendTo($('#buttons-left'));

    $('<button />', {
        'type': 'button',
        'class': 'info-button navbar-info navbar-toggle',
        'html': 'Info'
    }).appendTo($('.navbar-header'));

    $('.info-button').on('click', function () {
        showInfo();
    });
}

function showInfo() {
    // get dialog div
    var dialog = $('.bbs-modal-dialog');

    // adjust left and top position
    var windowWidth = $(window).width();
    var windowHeight = $(window).height();

    if (windowWidth < 768 || windowHeight < 600) {
        dialog.height('auto');
        dialog.width('auto')

        dialog.css('top', 0);
        dialog.css('left', 0);
        dialog.css('bottom', 0);
        dialog.css('right', 0);
    } else {
        dialog.height(530);
        dialog.width(660)

        var left = (windowWidth - dialog.width()) / 2;
        dialog.css('left', left);
        var top = (windowHeight - dialog.height()) / 2 - 20;
        dialog.css('top', top);
        dialog.css('bottom', 'auto');
        dialog.css('right', 'auto');
    }

    // show the modal
    $('.bbs-modal').show();

    // enable esc and enter keys
    $(document).keyup(function(e) {
        if (e.keyCode == 27 || e.keyCode == 13) {
            // esc pressed
            $('.bbs-modal').hide();
            return false;
        }
    });
    $('.leaflet-popup-close-button',dialog).on('click', function () {
        $('.bbs-modal').hide();
        return false;
    });
    $('.bbs-modal').on('click', function (e) {
        if($(e.target).is('.bbs-modal') !== true){
            e.preventDefault();
            return;
        }
        $('.bbs-modal').hide();
        return false;
    });
};

$(document).ready(function() {
    setTimeout('init()',100);
});
