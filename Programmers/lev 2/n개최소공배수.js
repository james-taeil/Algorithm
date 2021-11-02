const solution = (arr) => {
  let answer = 1;
  for (let i = 0; i < arr.length; i++) {
    answer = lcm(answer, arr[i]);
  }
  return answer;
}

const gcd = (num1, num2) => {
  if (num1 === 0) return num2;
  return gcd(num2 % num1, num1)
}

const lcm = (num1, num2) => {
  return (num1 * num2) / gcd(num1, num2);
}

let arr = [2,6,8,14];
console.log(solution(arr));