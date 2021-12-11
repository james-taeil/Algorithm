const solution = (n, m) => {
    const getRandomArbitrary = (min, max) => {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min; 
    }

    let arr = Array.from(Array(n), () => Array(m).fill(null));

    arr.map((el, idx) => {
        el.map((_, idx2) => {
            arr[idx][idx2] = getRandomArbitrary(1, 100);
        })
    })

    console.log(arr);
    

    return 
}

let n = 5;
let m = 6;
console.log(solution(n, m))