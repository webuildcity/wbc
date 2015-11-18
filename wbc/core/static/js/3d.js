// if (!window.wbc3d) {
//     window.wbc3d_conf = {};

//     // wbc3d_conf.DATADIR = '../data/';
//     wbc3d_conf.WORKERPATH = '../lib/vizicities/vizi-worker.min.js';
// }

$(document).ready(function(){

  wbc3d =function(div, coord, poly) {

    var centerLatLon = new VIZI.LatLon(coord);

    // VIZI.DEBUG = true;
    world = new VIZI.World({
      viewport: document.querySelector(div),
      // layersUI: true,
      center: centerLatLon,
    });

    // var pickControls = new VIZI.ControlsMousePick(world.camera, {
    //   scene: world.scene
    // });

    var controls = new VIZI.ControlsMap(world.camera, {
      viewport: world.options.viewport
    });

    var mapConfig = {
      input: {
        type: "BlueprintInputMapTiles",
        options: {
          tilePath: "http://tiles.we-build.city/hamburg/{z}/{x}/{y}.png"
          // tilePath: "http://b.tile.openstreetmap.org/{z}/{x}/{y}.png"
        }
      },
      output: {
        type: "BlueprintOutputImageTiles",
        options: {
          grids: [{
            zoom: 19,
            tilesPerDirection: 3,
            cullZoom: 16
          // }, {
          //   zoom: 18,
          //   tilesPerDirection: 3,
          //   cullZoom: 16
          // }, {
          //   zoom: 17,
          //   tilesPerDirection: 3,
          //   cullZoom: 15
          }, {
            zoom: 16,
            tilesPerDirection: 3,
            cullZoom: 12
          // }, {
          //   zoom: 15,
          //   tilesPerDirection: 3,
          //   cullZoom: 13
          // }, {
          //   zoom: 14,
          //   tilesPerDirection: 3,
          //   cullZoom: 12
           }, {
            zoom: 13,
            tilesPerDirection: 1,
            cullZoom: 11
           }]
        }
      },
      triggers: [{
        triggerObject: "output",
        triggerName: "initialised",
        triggerArguments: ["tiles"],
        actionObject: "input",
        actionName: "requestTiles",
        actionArguments: ["tiles"],
        actionOutput: {
          tiles: "tiles" // actionArg: triggerArg
        }
      }, {
        triggerObject: "output",
        triggerName: "gridUpdated",
        triggerArguments: ["tiles"],
        actionObject: "input",
        actionName: "requestTiles",
        actionArguments: ["tiles"],
        actionOutput: {
          tiles: "tiles" // actionArg: triggerArg
        }
      }, {
        triggerObject: "input",
        triggerName: "tileReceived",
        triggerArguments: ["image", "tile"],
        actionObject: "output",
        actionName: "outputImageTile",
        actionArguments: ["image", "tile"],
        actionOutput: {
          image: "image", // actionArg: triggerArg
          tile: "tile"
        }
      }]
    };

    var switchboardMap = new VIZI.BlueprintSwitchboard(mapConfig);
    switchboardMap.addToWorld(world);


  var buildingsConfig = {
    input: {
      type: "BlueprintInputGeoJSON",
      options: {
        tilePath: "http://vector.mapzen.com/osm/buildings/{z}/{x}/{y}.json"
      }
    },
    output: {
      type: "BlueprintOutputCustomBuildingTiles",
      options: {
        grids: [{
          zoom: 15,
          tilesPerDirection: 1,
          cullZoom: 13
        }],
        workerURL: window.wbc3d_conf.WORKERPATH,
        // excludeArray: excludeBuildingsConfig,
        bbox: window.polygonmesh
      }
    },
    triggers: [{
      triggerObject: "output",
      triggerName: "initialised",
      triggerArguments: ["tiles"],
      actionObject: "input",
      actionName: "requestTiles",
      actionArguments: ["tiles"],
      actionOutput: {
        tiles: "tiles" // actionArg: triggerArg
      }
    }, {
      triggerObject: "output",
      triggerName: "gridUpdated",
      triggerArguments: ["tiles", "newTiles"],
      actionObject: "input",
      actionName: "requestTiles",
      actionArguments: ["tiles"],
      actionOutput: {
        tiles: "newTiles" // actionArg: triggerArg
      }
    }, {
      triggerObject: "input",
      triggerName: "tileReceived",
      triggerArguments: ["geoJSON", "tile"],
      actionObject: "output",
      actionName: "outputBuildingTile",
      actionArguments: ["buildings", "tile"],
      actionOutput: {
        buildings: {
          process: "map",
          itemsObject: "geoJSON",
          itemsProperties: "features",
          transformation: {
            outline: "geometry.coordinates",
            height: "properties.height",
            minHeight: "properties.min_height",
            id: "properties.id"
          }
        },
        tile: "tile"
      }
    }]
  };

  var switchboardBuildings = new VIZI.BlueprintSwitchboard(buildingsConfig);
  switchboardBuildings.addToWorld(world);


  var polygonConfig = {
    input: {
      type: "BlueprintInputPolygon",
      options: {
        poly: poly
      }
    },
    output: {
      type: "BlueprintOutputPolygon",
      options: {
        colourRange: ["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"],
        layer: 100,
        infoUI: true,
        description: "Polygon"
      }
    },
    triggers: [{
      triggerObject: "output",
      triggerName: "initialised",
      triggerArguments: [],
      actionObject: "input",
      actionName: "requestData",
      actionArguments: [],
      actionOutput: {}
    }, {
      triggerObject: "input",
      triggerName: "dataReceived",
      triggerArguments: ["geoJSON"],
      actionObject: "output",
      actionName: "outputPolygon",
      actionArguments: ["data"],
      actionOutput: {
        data: {
          // Loop through each item in trigger.geoJSON and return a new array of processed values (a map)
          process: "map",
          itemsObject: "geoJSON",
          itemsProperties: "data",
          // Return a new object for each item with the given properties
          transformation: {
              outline: "geometry.coordinates[0]"
          }
        }
      }
    }]
  };

  var switchboardChoropleth = new VIZI.BlueprintSwitchboard(polygonConfig);
  switchboardChoropleth.addToWorld(world);


  // var reverseBuildingsConfig = {
  //   input: {
  //     type: "BlueprintInputGeoJSON",
  //     options: {
  //       tilePath: "http://vector.mapzen.com/osm/buildings/{z}/{x}/{y}.json"
  //     }
  //   },
  //   output: {
  //     type: "BlueprintOutputReverseFlatBuildingTiles",
  //     options: {
  //       grids: [{
  //         zoom: 15,
  //         tilesPerDirection: 1,
  //         cullZoom: 13
  //       }],
  //       workerURL: window.wbc3d_conf.WORKERPATH,
  //       excludeArray: excludeBuildingsConfig,
  //       bbox: bbox
  //     }
  //   },
  //   triggers: [{
  //     triggerObject: "output",
  //     triggerName: "initialised",
  //     triggerArguments: ["tiles"],
  //     actionObject: "input",
  //     actionName: "requestTiles",
  //     actionArguments: ["tiles"],
  //     actionOutput: {
  //       tiles: "tiles" // actionArg: triggerArg
  //     }
  //   }, {
  //     triggerObject: "output",
  //     triggerName: "gridUpdated",
  //     triggerArguments: ["tiles", "newTiles"],
  //     actionObject: "input",
  //     actionName: "requestTiles",
  //     actionArguments: ["tiles"],
  //     actionOutput: {
  //       tiles: "newTiles" // actionArg: triggerArg
  //     }
  //   }, {
  //     triggerObject: "input",
  //     triggerName: "tileReceived",
  //     triggerArguments: ["geoJSON", "tile"],
  //     actionObject: "output",
  //     actionName: "outputBuildingTile",
  //     actionArguments: ["buildings", "tile"],
  //     actionOutput: {
  //       buildings: {
  //         process: "map",
  //         itemsObject: "geoJSON",
  //         itemsProperties: "features",
  //         transformation: {
  //           outline: "geometry.coordinates",
  //           height: "properties.height",
  //           minHeight: "properties.min_height",
  //           id: "properties.id"
  //         }
  //       },
  //       tile: "tile"
  //     }
  //   }]
  // };

  // var switchboardReverseBuildings = new VIZI.BlueprintSwitchboard(reverseBuildingsConfig);
  // switchboardReverseBuildings.addToWorld(world);

    var clock = new VIZI.Clock();

    var update = function() {
      var delta = clock.getDelta();

      world.onTick(delta);
      world.render();

      window.requestAnimationFrame(update);
      // TWEEN.update();
    };

    update();

  //   function cameraflight(){
  //       // position = {x: 100, y: 0};
  //       // console.log("jupp")
  //       // var testTween = new Tween.Tween(position);
  //       // testTween.to({x:200}, 1000);
  //       // testTween.onUpdate(function() {
  //       //     console.log(this.x);
  //       // });
  //       // testTween.start();
  //       var camera = world.camera.camera;
  //       var current = {x: 0.5};
  //       var target = {x: 1.5};
  //       var tween = new TWEEN.Tween(current).to(target, 7000).easing(TWEEN.Easing.Linear.None);
  //       tween.onUpdate(function(){
  //         console.log("update");
  //         console.log(this);
  //         camera.position.x = 0 + 600 * Math.cos( 6 * this.x );         
  //         camera.position.z = 0 + 600 * Math.sin( 6 * this.x );
  //         camera.lookAt(new VIZI.Point(0,0,0));
  //       });
  //       tween.onComplete(function(){
  //         console.log("complete")
  //       });
  //       tween.start();
  //       console.log('start tween');
  //   }

  //   function tweenTo(position){
  //       var camera = world.camera.camera;
  //       var current = camera.position;
  //       var target = position;
  //       var tween = new TWEEN.Tween(current).to(target, 2500).easing(TWEEN.Easing.Quartic.Out);
  //       tween.onUpdate(function(){
  //         console.log("update");
  //         console.log(this);
  //         camera.position.x = this.x;         
  //         camera.position.z = this.z;
  //         camera.position.y = this.y;
  //         camera.lookAt(new VIZI.Point(0,75,0));
  //       });
  //       tween.onComplete(function(){
  //         console.log("complete")
  //       });
  //       tween.start();
  //       console.log('start tween');


  //   }
  //   //buttons
  //   var citygml = false;
  //   $('#citygml-switch').click(function(){
  //     if(citygml){
  //       world.layers[1].hide();
  //       world.layers[3].show();
  //       citygml = false;
  //     } else {
  //       world.layers[1].show();
  //       world.layers[3].hide();
  //       citygml = true;
  //     }
  //     // console.log("yo");
  //   });
  //   $('#camera-flight').click(function(){
  //     cameraflight();
  //   })
  //   $('#north').click(function(){
  //     tweenTo({x:0, y:200, z:-450});
  //   })
  //   $('#east').click(function(){
  //     tweenTo({x:450, y:200, z:0});
  //   })
  //   $('#south').click(function(){
  //     tweenTo({x:0, y:200, z:450});
  //   })
  //   $('#west').click(function(){
  //     tweenTo({x:-450, y:200, z:0});
  //   })
  }




});
