/* globals window, _, VIZI, d3 */
(function() {
  "use strict";

/**
 * Blueprint GeoJSON input
 * @author Robin Hawkes - vizicities.com
 */  

  // input: {
  //   type: "BlueprintInputGeoJSON",
  //   options: {
  //     path: "/data/tower-hamlets-lsoa-census.geojson"
  //     // tilePath: "http://vector.mapzen.com/osm/buildings/{z}/{x}/{y}.json"
  //   }
  // }

  var tileURLRegex = /\{([zxy])\}/g;

  VIZI.BlueprintInputPolygon = function(options) {
    var self = this;

    VIZI.BlueprintInput.call(self, options);

    _.defaults(self.options, {});

    // Triggers and actions reference
    self.triggers = [
      {name: "initialised", arguments: []},
      {name: "dataReceived", arguments: ["geoJSON"]},
    ];

    self.actions = [
      {name: "requestData", arguments: []},
    ];
  };

  VIZI.BlueprintInputPolygon.prototype = Object.create( VIZI.BlueprintInput.prototype );

  // Initialise instance and start automated processes
  VIZI.BlueprintInputPolygon.prototype.init = function() {
    var self = this;
    self.emit("initialised");
  };

  // TODO: Pull from cache if available
  VIZI.BlueprintInputPolygon.prototype.requestData = function() {
    var self = this;

    if (!self.options.poly) {
      throw new Error("Required poly option missing");
    }

    // Request data
    console.log(self.options.poly.toGeoJSON());
    var data = { 'data': self.options.poly.toGeoJSON()};
    self.emit("dataReceived", data);
  };

  // [{
  //   x: 262116,
  //   y: 174348,
  //   z: 19
  // }, ...]

  // TODO: Cache a certain amount of tiles
  // TODO: Pull from cache if available
}());