// Get your token from https://cesium.com/ion/tokens

// imports

// vars
Cesium.Ion.defaultAccessToken =
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0YWUyMWRmMS1jNDMwLTQxYTQtYTY4NC02YzViMDc4MzRhMGQiLCJpZCI6MjEwNTY2LCJpYXQiOjE3MTM4NDc3MDV9.tzUsn3XhbqICfw5zou-Qsk7XO_e7fqwAhnz0eKE9JlE";
const viewer = new Cesium.Viewer("cesiumContainer", {shouldAnimate: true});

// functions 
function openFiles(){
    window.open("file:///", '_blank'); // I doubt this'll work tbh 
}

function center(){
    viewer.flyTo(pointEntity);
}

function center2(){
    viewer.flyTo(pointEntity2)
}

function center7(){
    viewer.flyTo(pointEntity3)
}

// code 

// Static entity @ Howe
viewer.scene.primitives.add(Cesium.createOsmBuildings());
const dataPoint = { longitude: -74.023, latitude: 40.745, height: +27.32, freq: "5.0 GHz", power:"30 mW", bubble: "5 m"};
const pointEntity = viewer.entities.add({
    description: `First data point at (${dataPoint.longitude}, ${dataPoint.latitude}, ${dataPoint.height})\nPower: ${dataPoint.power},\nFrequency: ${dataPoint.freq}, \nBubble: ${dataPoint.bubble}`,
    position: Cesium.Cartesian3.fromDegrees(dataPoint.longitude, dataPoint.latitude, dataPoint.height),
    point: { pixelSize: 10, color: Cesium.Color.RED }
});

const dataPoint2 = { longitude: -74.083, latitude: 40.765, height: +600, freq: "2.4 GHz", power:"30 mW", bubble: "20 m"};
const pointEntity2 = viewer.entities.add({
    description: `First data point at (${dataPoint2.longitude}, ${dataPoint2.latitude}, ${dataPoint2.height})\nPower: ${dataPoint2.power},\nFrequency: ${dataPoint2.freq}, \nBubble: ${dataPoint2.bubble}`,
    position: Cesium.Cartesian3.fromDegrees(dataPoint2.longitude, dataPoint2.latitude, dataPoint2.height),
    point: { pixelSize: 20, color: Cesium.Color.BLUE }
});

const dataPoint3 = { longitude: -74.052, latitude: 40.722, height: +190, freq: "7.3 MHz", power:"42 mW", bubble: "9 m"};
const pointEntity3 = viewer.entities.add({
    description: `First data point at (${dataPoint3.longitude}, ${dataPoint3.latitude}, ${dataPoint3.height})\nPower: ${dataPoint3.power},\nFrequency: ${dataPoint3.freq}, \nBubble: ${dataPoint3.bubble}`,
    position: Cesium.Cartesian3.fromDegrees(dataPoint3.longitude, dataPoint3.latitude, dataPoint3.height),
    point: { pixelSize: 15, color: Cesium.Color.GREEN }
});


// Moving entity stuff 

//Make sure viewer is at the desired time.
const start = Cesium.JulianDate.fromDate(new Date(2018, 11, 12, 15));
const totalSeconds = 10;
const stop = Cesium.JulianDate.addSeconds(
  start,
  totalSeconds,
  new Cesium.JulianDate()
);
viewer.clock.startTime = start.clone();
viewer.clock.stopTime = stop.clone();
viewer.clock.currentTime = start.clone();
viewer.clock.clockRange = Cesium.ClockRange.LOOP_STOP;
viewer.timeline.zoomTo(start, stop);


// Create a path for our vehicle by lerping between two positions.
const position = new Cesium.SampledPositionProperty();
const startPosition = new Cesium.Cartesian3.fromDegrees(-74.034,40.749,70.000);
const endPosition  = new Cesium.Cartesian3.fromDegrees(-74.025,40.741,91);
// A velocity vector property will give us the entity's speed and direction at any given time.
const velocityVectorProperty = new Cesium.VelocityVectorProperty(
  position,
  false
);
const velocityVector = new Cesium.Cartesian3();
// Store the wheel's rotation over time in a SampledProperty.


const numberOfSamples = 100;
for (let i = 0; i <= numberOfSamples; ++i) {
  const factor = i / numberOfSamples;
  const time = Cesium.JulianDate.addSeconds(
    start,
    factor * totalSeconds,
    new Cesium.JulianDate()
  );

  // Lerp using a non-linear factor so that the vehicle accelerates.
  const locationFactor = Math.pow(factor, 2);
  const location = Cesium.Cartesian3.lerp(
    startPosition,
    endPosition,
    locationFactor,
    new Cesium.Cartesian3()
  );
  position.addSample(time, location);
  // Rotate the wheels based on how fast the vehicle is moving at each timestep.
  velocityVectorProperty.getValue(time, velocityVector);
  const metersPerSecond = Cesium.Cartesian3.magnitude(velocityVector);

}


// Add our vehicle model.
const vehicleEntity = viewer.entities.add({
  position: position,
  orientation: new Cesium.VelocityOrientationProperty(position), // Automatically set the vehicle's orientation to the direction it's facing.
  point: { pixelSize: 15, color: Cesium.Color.GREEN },

});




// calls 
viewer.flyTo(vehicleEntity);
