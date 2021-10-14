const solution = (id_list, report, k) => {
    let answer = [];
    let obj = {};
    let countObj = {};
    let reportPerson = [];
    let count = 0;

    // 신고한 사람 로직
    for (let i = 0; i < id_list.length; i++) {
        obj[id_list[i]] = [];
    }

    for (let i = 0; i < report.length; i++) {
        if (obj[report[i].split(' ')[0]].includes(report[i].split(' ')[1])) continue;
        else obj[report[i].split(' ')[0]].push(report[i].split(' ')[1]);
    }
    report = report.sort();
    console.log(report)
    // 신고당한 사람 로직
    for (let i = 0; i < report.length; i++) {
        if (countObj[report[i].split(' ')[1]] === undefined) {
            countObj[report[i].split(' ')[1]] = 1;
        } else if (report[i - 1].split(' ')[0] === report[i].split(' ')[0] && report[i - 1].split(' ')[1] === report[i].split(' ')[1]) {
            continue;
        } else {
            countObj[report[i].split(' ')[1]] += 1;
        }
        console.log(countObj)
    }    

    // k 조건에 맞는 신고당한 사람
    for (let key in countObj) {
        // console.log(countObj)
        if (countObj[key] >= k) {
            reportPerson.push(key)
        }
    }
    
    for (let key in obj) {
        for (let j = 0; j < reportPerson.length; j++) {
            if (obj[key].includes(reportPerson[j])) {
                count += 1;
            }
        }
        answer.push(count);
        count = 0;
    }
    // console.log(obj)
    // console.log(countObj)
    // console.log(reportPerson, 'reportPerson')

    return answer
    
}
    


let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k = 2;
console.log(solution(id_list, report, k));