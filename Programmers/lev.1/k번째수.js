function solution(array, commands) {
  let answer = [];

  for (let command of commands) {
    let [fristIdx, secondIdx, value]  = command;
    answer.push(array.slice(fristIdx-1, secondIdx).sort((a, b) => a - b)[value - 1]);
  }
  return answer;
}


let arr = [1, 5, 2, 6, 3, 7, 4];
let commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];
console.log(solution(arr, commands))

