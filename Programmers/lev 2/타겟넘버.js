const solution = (numbers, target) => {
    let answer = 0;
    const dfs = (lev, sum) => {
        if(lev === numbers.length) {
            if(sum === target) answer += 1;
            return;
        }

        dfs(lev + 1, sum + numbers[lev]);
        dfs(lev + 1, sum - numbers[lev]);        
    }
    dfs(0, 0);

    return answer;
}

let numbers = [1, 1, 1, 1, 1];
let target = 3;
console.log(solution(numbers, target));