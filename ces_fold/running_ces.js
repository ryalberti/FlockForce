// Get your token from https://cesium.com/ion/tokens
Cesium.Ion.defaultAccessToken =
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0YWUyMWRmMS1jNDMwLTQxYTQtYTY4NC02YzViMDc4MzRhMGQiLCJpZCI6MjEwNTY2LCJpYXQiOjE3MTM4NDc3MDV9.tzUsn3XhbqICfw5zou-Qsk7XO_e7fqwAhnz0eKE9JlE";
const viewer = new Cesium.Viewer("cesiumContainer");
viewer.scene.primitives.add(Cesium.createOsmBuildings());

const dataPoint = { longitude: -74.0323752, latitude: 40.7433066, height: +27.32 };
const pointEntity = viewer.entities.add({
    description: `First data point at (${dataPoint.longitude}, ${dataPoint.latitude})`,
    position: Cesium.Cartesian3.fromDegrees(dataPoint.longitude, dataPoint.latitude, dataPoint.height),
    point: { pixelSize: 10, color: Cesium.Color.RED }
});

viewer.flyTo(pointEntity);