function solution(a, b) {
    let answer = '';
    let weeks = ["THU","FRI","SAT","SUN","MON","TUE","WED"];
    let calender = {
        "1" : 31, "2" : 29, "3" : 31, "4" : 30, "5" : 31, "6" : 30,
        "7" : 31, "8" : 31, "9" : 30, "10" : 31, "11" : 30, "12" : 31
    }

    let day = b;

    for (let key in calender) {
        if (Number(key) !== a) day += calender[key];
        else break;
    }
    let idx = day % 7;
    answer = weeks[idx];

    return answer;
}

console.log(solution(5, 24));