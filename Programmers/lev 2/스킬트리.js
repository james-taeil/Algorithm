const solution = (skill, skill_trees) => {
    let answer = 0;
    let filterd = skill_trees.map((tree) => {
        return tree.split('').filter(el => skill.includes(el))
    });

    console.log(filterd);

    for(let i = 0; i < filterd.length; i++) {
        let isValid = true;
        for(let j = 0; j < filterd[i].length; j++) {
            if(skill[j] !== filterd[i][j]) {
                isValid = false;
                break;
            }
        }
        if(isValid) answer++;
    }
    return answer;
}

let skill = 'CBD';
let skill_trees = ["BACDE", "CBADF", "AECB", "BDA"];
console.log(solution(skill, skill_trees));