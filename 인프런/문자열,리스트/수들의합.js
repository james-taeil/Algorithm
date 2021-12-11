const solution = (n, m, nl) => {
    let answer = 0;
    let lt = 0;
    let rt = 1;
    let total = nl[0];

    while(true) {
        if (total < m) {
            if (rt < n) {
                total += nl[rt];
                rt += 1;
            } 
            else  break;
        } else if (total === m) {
            answer += 1;
            total -= nl[lt];
            lt += 1;
        } else {
            total -= nl[lt];
            lt += 1;
        }
    }   
    return answer;
}

let n = 8;
let m = 3;
let numberlist = [1,2,3,1,2,1,1,1];
console.log(solution(n, m, numberlist))