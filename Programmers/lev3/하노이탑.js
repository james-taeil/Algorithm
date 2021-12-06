const solution = (n) => {
    const answer = [];

    // n : 원반의 개수
    // src : 출발지 기둥
    // dst : 마지막 기둥
    // mid : 가운데 기둥
    const hanoi = (n, src, dst, mid) => { 
        if (n === 1) {
            answer.push([src, dst]);
        } else {
            hanoi(n - 1, src, mid, dst);
            answer.push([src, dst]);
            hanoi(n - 1, mid, dst, src);
        }
    }

    hanoi(n, 1, 3, 2);
    return answer;
}

let n = 2;
console.log(solution(n));