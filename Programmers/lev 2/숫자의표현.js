const solution = (n) => {
    // 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수와 주어진 수의 홀수인 약수 갯수는 같다.
    // 1 + 2 + 3 + 4 + 5 === 3 + 3 + 3 + 3 + 3
    let count = 0;

    for(let i = 0; i <= n; i++) {
        if(n % i === 0 && i % 2 === 1) count ++;
    }   
    
    return count;
}

let n = 15;
console.log(solution(n));