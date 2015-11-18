/* globals window, _, VIZI, d3, THREE */
(function() {
  "use strict";

/**
 * Blueprint choropleth output
 * @author Robin Hawkes - vizicities.com
 */

  // TODO: Animate hover and off effect for picking (opacity, scale, etc)
  // TODO: Show 2D info UI on hover or click

  // output: {
  //   type: "BlueprintOutputPolygon",
  //   options: {
  //     colourRange: ["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"],
  //     layer: 100
  //   }
  // }
  VIZI.BlueprintOutputPolygon = function(options) {
    var self = this;

    VIZI.BlueprintOutput.call(self, options);

    _.defaults(self.options, {
      colourRange: ["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"],
      layer: 10,
      keyUI: true,
      infoUI: false,
      name: "Polygon"
    });

    // Triggers and actions reference
    self.triggers = [
      {name: "initialised", arguments: []}
    ];

    self.actions = [
      {name: "outputPolygon", arguments: ["data"]}
    ];

    self.name = self.options.name;

    self.world;
    self.keyUI;
    self.infoUI;

    self.pickedMesh;
    self.lastPickedIdClick;
  };

  VIZI.BlueprintOutputPolygon.prototype = Object.create( VIZI.BlueprintOutput.prototype );

  // Initialise instance and start automated processes
  VIZI.BlueprintOutputPolygon.prototype.init = function() {
    var self = this;

    // Set up key UI
    if (self.options.keyUI) {
      self.keyUI = new VIZI.KeyUIColourScale(self);
    }

    // Set up info UI
    if (self.options.infoUI) {
      self.infoUI = new VIZI.InfoUI2D(self.world);
    }

    self.emit("initialised");
  };

  // {
  //   outline: [],
  //   value: 123
  // }
  VIZI.BlueprintOutputPolygon.prototype.outputPolygon = function(data) {
    var self = this;

    // console.log(data);
    var material = new THREE.MeshLambertMaterial({
      vertexColors: THREE.VertexColors,
      ambient: 0xffffff,
      emissive: 0xcccccc,
      shading: THREE.FlatShading,
      // TODO: Remove this by implementing logic to make points clockwise
      side: THREE.BackSide,
      transparent: true, 
      opacity: 0.5
    });

    // Choropleth range settings
    // if (self.options.colourRange) {
    //   // Sort feature data in order
    //   var dataValues = data.sort(function(a, b) {
    //     return d3.ascending(Number(a.value), Number(b.value));
    //   });

    //   var lo = Number(dataValues[0].value);
    //   var hi = Number(dataValues[data.length - 1].value);

    //   // TODO: Decouple range values
    //   var scale = d3.scale.linear()
    //     .domain([lo, hi])
    //     .range([1, 500]);

    //   var scaleColour = d3.scale.quantile()
    //     .domain([lo, hi])
    //     .range(self.options.colourRange);

    //   var breakCount = scaleColour.range().length;
    //   var keyScale = scaleColour.range().map(function(value, index) {
    //     var key;
    //     if (index === 0) {
    //       key = Number(lo.toFixed(2)) + " - " + Number(scaleColour.quantiles()[index].toFixed(2));
    //     } else if (index === breakCount - 1) {
    //       key = Number(scaleColour.quantiles()[index-1].toFixed(2)) + " - " + Number(hi.toFixed(2));
    //     } else {
    //       key = Number(scaleColour.quantiles()[index-1].toFixed(2)) + " - " + Number(scaleColour.quantiles()[index].toFixed(2));
    //     }

    //     return {
    //       colour: value,
    //       key: key
    //     }
    //   });

    //   if (self.keyUI) {
    //     self.keyUI.scale = keyScale;
    //     self.keyUI.onChange();
    //   }
    // }

    var combinedGeom = new THREE.Geometry();
    data = [ data ];
    _.each(data, function(feature) {
      var offset = new VIZI.Point();
      var shape = new THREE.Shape();
      
      _.each(feature[0].outline[0], function(coord, index) {
        var geoCoord = self.world.project(new VIZI.LatLon(coord[1], coord[0]));
        if (offset.length === 0) {
          offset.x = -1 * geoCoord.x;
          offset.y = -1 * geoCoord.y;
        }

        // Move if first coordinate
        if (index === 0) {
          shape.moveTo( geoCoord.x + offset.x, geoCoord.y + offset.y );
        } else {
          shape.lineTo( geoCoord.x + offset.x, geoCoord.y + offset.y );
        }
      });
      var extrudeSettings = { amount: -5, bevelEnabled: true, bevelSegments: 2, steps: 2, bevelSize: 1, bevelThickness: 1 };
      var geom = new THREE.ExtrudeGeometry( shape, extrudeSettings );

    //   // Use choropleth range colour if defined, else random
      var colour = new THREE.Color(0xffffff * Math.random());

      self.applyVertexColors(geom, colour);

      var mesh = new THREE.Mesh(geom);

      // Offset
      mesh.position.x = -1 * offset.x;
      mesh.position.z = -1 * offset.y;

      // TODO: Provide Y offset in options (to avoid clashing with floor, etc)
      // mesh.position.y = 1;

      // Flip as they are up-side down
      // TODO: Remove this by implementing logic to make points clockwise
      mesh.rotation.x = 90 * Math.PI / 180;

      mesh.matrixAutoUpdate && mesh.updateMatrix();
      combinedGeom.merge(mesh.geometry, mesh.matrix);

    //   // Make choropleth element clickable
    //   // TODO: Should this reference the geom.id or mesh.id?
      self.world.addPickable(mesh, geom.id);

      VIZI.Messenger.on("pick-hover:" + geom.id, function() {
        // Do nothing if hidden
        if (self.hidden) {
          return;
        }

        if (self.pickedMesh) {
          self.remove(self.pickedMesh);
        }

        var geomCopy = geom.clone();

        self.pickedMesh = new THREE.Mesh(geomCopy, new THREE.MeshBasicMaterial({
          color: 0xff0000,
          // TODO: Remove this by implementing logic to make points clockwise
          side: THREE.BackSide,
          depthWrite: false,
          transparent: true
        }));

        var offset = geomCopy.center();

        // Use previously calculated offset to return merged mesh to correct position
        // This allows frustum culling to work correctly
        self.pickedMesh.position.x = -1 * offset.x;

        // Removed for scale center to be correct
        // Offset with applyMatrix above
        self.pickedMesh.position.y = -1 * offset.z;

        // TODO: Why is Y the Z offset here?
        // Is it because the choropleth objects are flipped at 90 degrees?
        self.pickedMesh.position.z = -1 * offset.y;

        // self.pickedMesh.position.copy(mesh.position);

        self.pickedMesh.rotation.copy(mesh.rotation);
        self.pickedMesh.scale.copy(mesh.scale);

        self.pickedMesh.renderDepth = -1.1 * self.options.layer;

        self.pickedMesh.matrixAutoUpdate && self.pickedMesh.updateMatrix();

        self.add(self.pickedMesh);
      });

      VIZI.Messenger.on("pick-off:" + geom.id, function() {
        if (self.pickedMesh) {
          self.remove(self.pickedMesh);
        }
      });

      VIZI.Messenger.on("pick-click:" + geom.id, function() {
        // Do nothing if hidden
        if (self.hidden) {
          return;
        }

        // console.log("Clicked:", geom.id);
        var pickedId;

        // Create info panel
        if (self.infoUI) {
          if (self.lastPickedIdClick) {
            self.infoUI.removePanel(self.lastPickedIdClick);
            pickedId = undefined;
          }

          if (!self.lastPickedIdClick || self.lastPickedIdClick !== self.pickedMesh.id) {
            self.infoUI.addPanel(self.pickedMesh, feature.value);
            pickedId = self.pickedMesh.id;
          }
        }

        self.lastPickedIdClick = pickedId;
      }); 
    });

    // // Move merged geom to 0,0 and return offset
    var offset = combinedGeom.center();

    var combinedMesh = new THREE.Mesh(combinedGeom, material);

    if (self.options.layer.toString().length > 0) {
      combinedMesh.renderDepth = -1 * self.options.layer;
      combinedMesh.material.depthWrite = false;
      combinedMesh.material.transparent = true;
    }

    // Use previously calculated offset to return merged mesh to correct position
    // This allows frustum culling to work correctly
    combinedMesh.position.x = -1 * offset.x;

    // Removed for scale center to be correct
    // Offset with applyMatrix above
    combinedMesh.position.y = -1 * offset.y;

    combinedMesh.position.z = -1 * offset.z;
    // globmesh = combinedMesh;
    self.add(combinedMesh);
    window.polygonmesh = combinedMesh;
  };

  VIZI.BlueprintOutputPolygon.prototype.onHide = function() {
    var self = this;

    if (self.keyUI) {
      self.keyUI.onHide();
    }

    if (self.infoUI) {
      self.infoUI.onHide();
    }
  };

  VIZI.BlueprintOutputPolygon.prototype.onShow = function() {
    var self = this;

    if (self.keyUI) {
      self.keyUI.onShow();
    }

    if (self.infoUI) {
      self.infoUI.onShow();
    }
  };

  VIZI.BlueprintOutputPolygon.prototype.onTick = function(delta) {
    var self = this;

    // Update panel positions
    // TODO: Work out how to remove the visible lag between panel position
    // and actual scene / camera position.
    if (self.infoUI) {
      self.infoUI.onChange();
    }
  }

  VIZI.BlueprintOutputPolygon.prototype.onAdd = function(world) {
    var self = this;
    self.world = world;
    self.init();
  };
}());