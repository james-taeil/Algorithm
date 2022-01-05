const solution = (rows, columns, queries) => {
    let answer = [];
    let arr = Array.from(Array(rows), () => Array(columns).fill(null));
    let num = 1;

    arr.map((el, idx) => {
        el.map((_, idx2) => {
            arr[idx][idx2] = num;
            num += 1;
        })
    })

    queries.forEach((query) => {
        const [x1, y1, x2, y2] = query.map(pos => pos - 1);
        const dequeue = [];
        
        for(let i = y1; i < y2; i++) dequeue.push(arr[x1][i]);
        for(let i = x1; i < x2; i++) dequeue.push(arr[i][y2]);
        for(let i = y2; i > y1; i--) dequeue.push(arr[x2][i]);
        for(let i = x2; i > x1; i--) dequeue.push(arr[i][y1]);
        
        answer.push(Math.min(...dequeue));
        const temp = dequeue.pop();
        dequeue.unshift(temp);

        for(let i = y1; i < y2; i++) arr[x1][i] = dequeue.shift();
        for(let i = x1; i < x2; i++) arr[i][y2] = dequeue.shift();
        for(let i = y2; i > y1; i--) arr[x2][i] = dequeue.shift();
        for(let i = x2; i > x1; i--) arr[i][y1] = dequeue.shift();
    })

    return answer;
}



let rows = 6;
let columns = 6;
let queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]];
console.log(solution(rows, columns, queries));