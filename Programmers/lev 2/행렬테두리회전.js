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

    console.log(arr);

    return answer;
}

let rows = 6;
let columns = 6;
let queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]];
console.log(solution(rows, columns, queries));