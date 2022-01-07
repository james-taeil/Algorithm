const solution = (n) => {
    const getRandomArbitrary = (min, max) => {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min; 
    }

    const board = Array.from(Array(n), () => Array(n).fill(0));

    board.map((el, idx) => {
        el.map((_, idx2) => {
            board[idx][idx2] = getRandomArbitrary(1, 100);
        })
    })
    
    console.log(board);
    let answer = 0;
    s = parseInt(n / 2);
    e = parseInt(n / 2);
    for(let i = 0; i < n; i++) {
        for(let j = s; j < e + 1; j++) {
            answer += board[i][j];
            console.log(board[i][j])
        }
        if(i < parseInt(n / 2)) {
            s--;
            e++;
        } else {
            s++;
            e--;
        }
    }
    return answer;
}

let n = 5;
console.log(solution(n));