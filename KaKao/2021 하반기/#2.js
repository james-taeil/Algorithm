function isPrime (num) {
    if (num < 2) return false;
    if (num === 2) return true;

    for(let i = 2; i <= Math.floor(Math.sqrt(num)); i++){
        if (num % i === 0) {
          return false; 
        }
    }
    return true; 
}

function solution(n, k) {
    let answer = -1;
    let kNotation = String(n.toString(k));
    let count = 0;
    
    kNotation = kNotation.split('0');
    
    for (let i = 0; i < kNotation.length; i++) {
        if (isPrime(Number(kNotation[i]))) {
            count += 1;
        }
    }
    answer = count;

    return answer;
}

let n = 437674;
let k = 3;

console.log(solution(n, k));
