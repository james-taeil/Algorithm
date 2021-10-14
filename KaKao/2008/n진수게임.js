function solution(n, t, m, p) {
    let answer = '';
    let str = '';
    for (let i = 0; i <= m * t; i++) {
        str += i.toString(n).toUpperCase();
    }

    // let i = 0;
    // while (str.length < m * t) {
    //     str += i.toString(n).toUpperCase();
    //     i++
    // }
    
    str = str.slice(0, m*t);
    
    answer = str.split('').filter((el, idx) => idx % m === p - 1).join('')
    
    
    return answer;
}