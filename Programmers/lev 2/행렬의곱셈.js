function solution(arr1, arr2) {
    let answer = [];

    for (let i = 0; i < arr1.length; i++) {
        // 행렬 A의 행 접근 - A
        const row = arr1[i];
        answer.push([]);
        for (let j = 0; j < arr2[0].length; j++) {
          let sum = 0;
          for (let k = 0; k < arr2.length; k++) {
            sum += row[k] * arr2[k][j];
          }
          answer[i].push(sum);
        }
      }
    
    return answer;
}

let arr1 = [[1, 4], [3, 2], [4, 1]];
let arr2 = 	[[3, 3], [3, 3]];
console.log(solution(arr1, arr2));