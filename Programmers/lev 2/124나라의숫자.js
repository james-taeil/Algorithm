function solution (n) {
    let answer = '';
    const numlist = [4, 1, 2];

    while (n) {
        answer = numlist[n % 3] + answer;
        if (n % 3 === 0) {
            n = n / 3 - 1
        } else {
            n = Math.floor(n / 3);
        }
    }
    return answer;
}