var layers = {};
var verfahrensschritte;
var orte;

function init() {
    $.ajax({
        url: '/verfahrensschritte/',
        type: 'GET',
        dataType: 'json',
        headers: {
            'Accept': 'application/json'
        },
        error: self.ajaxError,
        success: function (json) {
            verfahrensschritte = json;

            var now = new Date().toISOString().match(/(\d+-\d+-\d+)/)[0];
            $.ajax({
                url: '/orte/?ende=' + now,
                type: 'GET',
                dataType: 'json',
                headers: {
                    'Accept': 'application/json'
                },
                error: self.ajaxError,
                success: function (json) {
                    orte = json.features;
                    initMap();
                }
            });
        }
    }); 
}

function initMap() {
    // add the map layer
    var map = new L.Map("map");
    var min = 9;
    var max = 17;
    var myLayer = new L.TileLayer('http://tiles.jochenklar.de/tiles/bbs/berlin/{z}/{x}/{y}.png', {
        minZoom: min,
        maxZoom: max,
        attribution: 'Map data &copy; 2012 OpenStreetMap contributors',
        zIndex: 0,
        errorTileUrl: 'http://tiles.jochenklar.de/bbs/error.png',
        reuseTiles: true
    });
    map.addLayer(myLayer);

    // center map
    var center = new L.LatLng(52.51, 13.37628);
    map.setView(center, 11);
    
    // add a layer for the old publications
    var greyIcon = L.icon({
        iconUrl: '/static/img/Baustellenschilder/klein/schild_grau_blass.png',    
        iconSize:     [26, 45], // size of the icon width,height    
        iconAnchor:   [13, 45], // point of the icon which will correspond to marker's location    
        popupAnchor:  [0, -46] // point from which the popup should open relative to the iconAnchor
    });  

    $.each(verfahrensschritte, function(key, vs) {
        var layer = {}

        layer.iconUrl = '/static/' + vs.icon;
        layer.hoverIconUrl = '/static/' + vs.hoverIcon;

        layer.icon = L.icon({
            iconUrl: '/static/' + vs.icon,
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

    // add points to map
    $.each(orte, function(key, ort){

        // get the first veroeffentlichung
        var veroeffentlichung = ort.properties.veroeffentlichungen[0]

        // get the id of the verfahrensschritt
        var vspk = veroeffentlichung.verfahrensschritt.pk;

        // get coordinates
        var lat = ort.geometry.coordinates[1];
        var lon = ort.geometry.coordinates[0];

        // create marker
        var marker = L.marker([lat,lon], {icon: layers[vspk].icon}); 
        marker.icon = layers[vspk].iconUrl;
        marker.hoverIcon = layers[vspk].hoverIconUrl;
        marker.on("mouseover", function(e) {
            e.target._icon.src = this.hoverIcon;
        }).on("mouseout", function(e) {
            e.target._icon.src = this.icon;
        });

        var popuptext = '<p><b>' + veroeffentlichung.verfahrensschritt.verfahren + '</b>';
        popuptext += '<p><i>' + veroeffentlichung.verfahrensschritt.name + '</i>';
        popuptext += ' <a href="/begriffe/#'+ vspk + '" >(?)</a></p>';
        popuptext += '<p>Betrifft Gegend um: ' + ort.properties.adresse + '</p>';
        popuptext += '<p>Verantwortlich: ' + veroeffentlichung.behoerde + '</p>';
        popuptext += '<p>Beteiligung möglich bis: ' + veroeffentlichung.ende + '</p>';
        popuptext += '<p><a href="/orte/' + ort.properties.pk + '" >Details</a></p>';

        marker.bindPopup(popuptext, {
            autoPanPaddingTopLeft: new L.Point(10,100),
            autoPanPaddingBottomRight: new L.Point(10,0)
        });
        marker.addTo(map);

        layers[vspk].layerGroup.addLayer(marker);
    }); 
        
    // bin the checkbox to load the old markers
    $('input[name=old]').click(function(){
        console.log('TODO');
    });
    
    // remove and add the zoom buttons
    var zoom = $('.leaflet-control-zoom').remove();
    zoom.appendTo($('#buttons-left'));
    $('.leaflet-control-attribution').remove();
    $('<div />', {
        'class': 'leaflet-control-zoom leaflet-bar leaflet-control pull-left',
        'html': '<a class="info-button leaflet-control-zoom-out" href="#" title="Info">?</a>'
    }).appendTo($('#buttons-left'));

    // add the info button
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
