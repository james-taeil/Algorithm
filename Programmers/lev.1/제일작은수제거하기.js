function solution (arr) {
  arr.splice(arr.indexOf(Math.min(...arr)), 1);
  console.log(arr);
  return arr.length ? arr : [-1];
}

let arr = [4,3,2,1];
console.log(solution(arr));