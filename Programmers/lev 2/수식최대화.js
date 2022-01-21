const solution = (expression) => {
    const priors = [
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['*', '+', '-'],
        ['*', '-', '+'],
    ];

    let sums = [];

    for(let prior of priors) {
        const reg = expression.split(/(\D)/);
        for(let exp of prior) {
            while(reg.includes(exp)) {
                let idx = reg.indexOf(exp);
                reg.splice(idx - 1, 3, eval(reg.slice(idx - 1, idx + 2).join('')));
            }
        }
        sums.push(Math.abs(reg[0]));
    }
    return Math.max(...sums);
}

let expression = "100-200*300-500+20";
console.log(solution(expression));