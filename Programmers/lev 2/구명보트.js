const solution = (people, limit) => {
    let answer = 0;
    let len = people.length - 1;
    let start = 0;
    people.sort((a, b ) => b - a);
    
    while(start < len) {
        let sum = people[start] + people[len];
        if(sum > limit) {
            start++;
        } else {
            start++;
            len--;
        }

        answer++;
    }

    if(start === len) answer++;

    return answer;
}

let people = [70, 50, 80, 50];
let limit = 100;
console.log(solution(people, limit));