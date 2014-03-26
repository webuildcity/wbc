var _map;
var _icons = [];
var _greyIcon;
var _markerLayer;
var _old = false;

function init() {
    // get the verfahrensschritte by ajax and call initMap
    $.ajax({
        url: '/verfahrensschritte/',
        dataType: 'json',
        headers: {'Accept': 'application/json'},
        success: function (json) {
            initMap(json);
        }
    }); 
}

function initMap(verfahrensschritte) {
    // add the map layer
    _map = new L.Map("map");
    var min = 9;
    var max = 17;
    var mapLayer = new L.TileLayer('http://tiles.buergerbautstadt.de/berlin/{z}/{x}/{y}.png', {
        minZoom: min,
        maxZoom: max,
        attribution: 'Map data &copy; 2012 OpenStreetMap contributors',
        zIndex: 0,
        errorTileUrl: 'http://tiles.buergerbautstadt.de/error.png',
        reuseTiles: true
    });
    _map.addLayer(mapLayer);

    // center map
    var center = new L.LatLng(52.51, 13.37628);
    _map.setView(center, 11);
    
    // add a layer for the markers
    _markerLayer = L.layerGroup().addTo(_map);

    // create icons for verfahrensschritte
    $.each(verfahrensschritte, function(key, verfahrensschritt) {
        _icons[verfahrensschritt.pk] = {
            icon : L.icon({
                iconUrl: verfahrensschritt.icon,
                iconSize:     [26, 45], 
                iconAnchor:   [13, 45],
                popupAnchor:  [0, -46]
            }),
            iconUrl: verfahrensschritt.icon,
            hoverIconUrl: verfahrensschritt.hoverIcon
        }
    });

    // add a layer for the old publications
    _greyIcon  = {
        icon : L.icon({
            iconUrl: '/static/img/Baustellenschilder/klein/schild_grau_blass.png',    
            iconSize:     [26, 45],
            iconAnchor:   [13, 45],
            popupAnchor:  [0, -46]
        })
    }; 

    // bin the checkbox to load the old markers
    $('input[name=old]').click(function(){
        _markerLayer.clearLayers();
        var url;
        var now = new Date().toISOString().match(/(\d+-\d+-\d+)/)[0];

        if (_old) {
            url = '/orte/?nach=' + now;
            _old = false;
        } else {
            url = '/orte/?vor=' + now;
            _old = true;
        }

        $.ajax({
            url: url,
            dataType: 'json',
            headers: {
                'Accept': 'application/json'
            },
            error: self.ajaxError,
            success: function (json) {
                _orte = json.features;
                initOrte()
            }
        });
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

    // load and display the orte with ende in the future
    var now = new Date().toISOString().match(/(\d+-\d+-\d+)/)[0];
    $.ajax({
        url: '/orte/?nach=' + now,
        type: 'GET',
        dataType: 'json',
        headers: {
            'Accept': 'application/json'
        },
        error: self.ajaxError,
        success: function (json) {
            _orte = json.features;
            initOrte();
        }
    });
}

function initOrte() {
    var markers = [];

    // add points to map
    $.each(_orte, function(key, ort){
        // get the first veroeffentlichung
        var veroeffentlichung = ort.properties.veroeffentlichungen[0]

        // get the id of the verfahrensschritt
        var vspk = veroeffentlichung.verfahrensschritt.pk;

        // get coordinates
        var lat = ort.geometry.coordinates[1];
        var lon = ort.geometry.coordinates[0];

        var icon;
        if (_old) {
            icon = _greyIcon;
        } else {
            icon = _icons[vspk]
        }

        // create marker
        var marker = L.marker([lat,lon], {icon: icon.icon});

        // enable hover icon
        if (!_old) {
            marker.iconUrl = icon.iconUrl
            marker.hoverIconUrl = icon.hoverIconUrl

            marker.on("mouseover", function(e) {
                e.target._icon.src = this.hoverIconUrl;
            }).on("mouseout", function(e) {
                e.target._icon.src = this.iconUrl;
            });
        }

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

        _markerLayer.addLayer(marker);
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
