function solution(s) {
    let answer = '';
    let arr = s.split(' ').map((el) => +el).sort((a, b) => a - b);
    answer = `${String(arr[0])} ${String(arr[arr.length - 1])}`;
    
    return answer;
}