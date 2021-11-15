const solution = (n) => {
    let answer = 0;
    for (let num of String(n)) {
        answer += +num;
    }
    return answer;
}

let n = 123;
console.log(solution(n));