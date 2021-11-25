function solution(progresses, speeds) {
    let answer = [];
    let powers = [];

    // 일률 배열 만들기
    for (let i = 0; i < progresses.length; i++) {
        let power = Math.ceil((100 - progresses[i]) / speeds[i]);
        powers.push(power)
    }

    while (powers.length > 0) {
        // 첫번째 숫자보다 큰 숫자 인덱스 번호 찾기
        let compareNumIndex = powers.findIndex(el => powers[0] < el);

        if (compareNumIndex >= 0) {
            answer.push(compareNumIndex);
            powers.splice(0, compareNumIndex);
        } else {
            answer.push(powers.length);
            powers.splice(0, powers.length);
        }
    }

    return answer;
}