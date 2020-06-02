export default function getVantaOptions(num_people) {
  let height = 10;
  let color = 7783424;
  let waveSpeed = 0.5;

  if (num_people > 15) {
    color = 8192257;
    waveSpeed = 2;
  } else if (num_people > 10) {
    color = 12870144;
    waveSpeed = 1.5;
  } else if (num_people > 5) {
    color = 7830785;
    waveSpeed = 1;
  }
  return {
    el: "#background",
    color: color,
    waveHeight: height,
    shininess: 10,
    waveSpeed: waveSpeed,
    zoom: 1.5
  };
}
