function solution(n) {
    let nString = Number(n).toString(2);
    let nCount = nString.match(/1/g).length;

    while(true) {
        n += 1;
        let nNext = Number(n).toString(2);
        let nextCount = nNext.match(/1/g).length;
        
        if(nCount === nextCount) {
            break;
        }
    }
    return n;
}

let n = 78;
console.log(solution(n));