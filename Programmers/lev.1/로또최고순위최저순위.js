function solution (lottos, win_nums) {    
    
    // * ==========[정답과 맞은 순(ex 6개 다 맞았다면 1등을 뽑을 수 있다.(6번 index))]==========
    const rank = [6, 6, 5, 4, 3, 2, 1];

    // * ==========[정답과 맞은 숫자 갯수]==========
    let answerCount = lottos.filter(lotto => win_nums.find(num => num === lotto)).length;

    // * ==========[0 갯수]==========
    let zeroCount = lottos.filter(lotto => lotto === 0).length;
    console.log(zeroCount)
    return [rank[answerCount + zeroCount], rank[answerCount]]
}

let lottos = [44, 1, 0, 0, 31, 25];
let win_nums = [31, 10, 45, 1, 6, 19];

console.log(solution(lottos, win_nums))