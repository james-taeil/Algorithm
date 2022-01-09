const solution = (n, commands) => {
    const getRandomArbitrary = (min, max) => {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }

    let s = 0;
    let e = n - 1;
    let answer = 0;
    const board = Array.from(Array(n), () => Array(n).fill(0));

    board.map((el, idx) => {
        el.map((_, idx2) => {
            board[idx][idx2] = getRandomArbitrary(1, 100);
        })
    })

    for(let i = 0; i < commands.length; i++) {
        let [row, dir, count] = commands[i];
        row -= 1;
        
        if(dir === 0) {
            for(let j = 0; j < count; j++) {
                let temp = board[row].shift();
                board[row].push(temp);
            }
        } else {
            for(let j = 0; j < count; j++) {
                let temp = board[row].pop();
                board[row].unshift(temp);
            }
        }
    }
    console.log(board);
    for(let i = 0; i < n; i++) {
        for(let j = s; j < e + 1; j++) {
            console.log(board[i][j]);
            answer += board[i][j];
        }
        if(i < parseInt(n / 2)) {
            s++;
            e--;
        } else {
            s--;
            e++;
        }
    }
    return answer;
}

let n = 5;
let commands = [[2, 0, 3], [5, 1, 2], [3, 1, 4]];
console.log(solution(n, commands));