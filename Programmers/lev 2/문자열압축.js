const solution = (s) => {
  let answer = 0;
  let arr = [];

  for (let j = 1; j < parseInt(s.length / 2); j++) {
    for (let i = 0; i < s.length; i+=j) {
      let current = s.substr(i, j);
      let next = s.substr(i + j, j);
      console.log(current, next);
    }
  }

}

let s = "aabbaccc";
console.log(solution(s));