const solution = (bridge_length, weight, truck_weights) => {
  let time = 0;
  let bridge = Array.from({length: bridge_length}, () => 0);

  while (true) {
    bridge.shift();
    bridge.push(0);
    time += 1;

    let nowWeight = bridge.reduce((prev, curr) => prev + curr);

    if ((nowWeight + truck_weights[0]) <= weight) {
      const truck = truck_weights.shift();
      bridge[bridge_length - 1] = truck;
      nowWeight += truck;
    }
    if (nowWeight === 0) {
      break;
    }
  }
  return time;
}

let bridge_length = 2;
let weight = 10;
let truck_weights = [7, 4, 5, 6];
console.log(solution(bridge_length, weight, truck_weights));