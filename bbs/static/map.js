var layers = {};

function initMap() {   
    var map = new L.Map("map");

    var min = 11;
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
        popuptext += ' <a href="/info/#'+ point.vspk + '" >(?)</a></p>';
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
        popuptext += ' <a href="/info/#'+ point.vspk + '" >(?)</a></p>';
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

    var info = $('<div />', {
        'class': 'leaflet-control-zoom leaflet-bar leaflet-control pull-left',
        'html': '<a id="info-button" class="leaflet-control-zoom-out" href="#" title="Info">i</a>'
    }).appendTo($('#buttons-left'));

    $('#info-button').on('click', function () {
        displayInfo();
    });
}

function displayInfo() {
    var html = '<h2>Worum geht es hier?</h2><p>Bevor in Berlin gebaut werden kann, müssen dafür häufig erst die rechtlichen Grundlagen geschaffen werden. So kann es beispielsweise sein, dass bevor ein Haus gebaut werden darf, erst der entsprechende <strong>Bebauungsplan</strong> geändert werden muss. Bei großen infrastrukturellen Bauvorhaben wie beispielsweise dem Bau einer Autobahn, muss meist ein <strong>Planfeststellungsverfahren</strong> durchgeführt werden.</p><p>In beiden Fällen – dem Bebauungsplanverfahren also auch dem Planfeststellungsverfahren – ist die Beteiligung der Bürger vorgesehen. Das heißt, dass die Pläne über einen bestimmten Zeitraum (meist um die vier  Wochen) öffentlich ausgelegt werden müssen und Bürger sich – je nach Verfahren –  dazu äußern können, Einwendungen einreichen können oder Ideen einbringen können. Die Informationen, welche Pläne wann, wo und wie lange ausliegen, werden im Amtsblatt, in den Printausgaben regionaler Zeitungen oder – in Berlin – auf diversen Webseiten veröffentlicht. Problem dabei ist, dass sie so für Bürger meist schwer zu finden sind. Mithilfe unserer Webseite BürgerBautStadt wollen wir das ändern.</p><h2>Welche Daten werden auf der Karte angezeigt?</h2><p>Die Marker auf der Karte stehen für Orte, an denen ein Bauvorhaben geplant ist und zu dem gerade die Planungsunterlagen – da zum Beispiel der Bebauungsplan geändert werden muss – ausliegen. Sobald die die Beteiligungsfrist abgelaufen ist, verschwinden die Marker von der Karte. Die angezeigten Informationen stammen alle aus dem wöchentlich erscheinendem Amtsblatt von Berlin, das wir mit Unterstützung der Naturschutzverbände manuell auswerten. Eine Liste aller seit Projektbeginn im Februar 2013 eingetragenen Informationen ist hier zu finden. Neben der Karten -und Listenansicht ist es auch möglich, die Informationen zu abonnieren - das heißt Interessierte können ihre Email-Adresse für bestimmte Bezirke angeben und erhalten automatisch eine Email, wenn etwas neues ausliegt.</p>';

    var modal = $('<div />',{
        'html': '<div class="bbs-modal-dialog"><div class="bbs-modal-dialog-close"><a class="leaflet-popup-close-button" href="#close">×</a></div><div class="bbs-modal-dialog-body">' + html + '</div></div>',
        'class': 'bbs-modal'
    }).appendTo('#wrapper');

    // // get dialog div
    var dialog = $('.bbs-modal-dialog');

    // adjust height and width
    dialog.height(500);
    dialog.width(700);

    // adjust left and top margin
    var leftMargin = ($(window).width() - dialog.width()) / 2;
    dialog.css('marginLeft', leftMargin);
    var topMargin = ($(window).height() - dialog.height()) / 2 - 20;
    dialog.css('marginTop', topMargin);

    // enable esc and enter keys
    $(document).keyup(function(e) {
        if (e.keyCode == 27 || e.keyCode == 13) {
            // esc pressed
            $('.bbs-modal').remove();
            return false;
        }
    });
    $('.leaflet-popup-close-button',dialog).on('click', function () {
        $('.bbs-modal').remove();
        return false;
    });
};

$(document).ready(function() {
    setTimeout('initMap()',100);
});
