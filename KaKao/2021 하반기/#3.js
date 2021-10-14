function sortObj(obj) {
    return Object.keys(obj).sort().reduce(function (result, key) {
      result[key] = obj[key];
      return result;
    }, {});
  }

function money (fees, time) {
    if (time <= fees[0]) {
        return fees[1];
    }
    let charge =  Math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
    return charge;
} 

function solution(fees, records) {
    let answer = [];
    let arr = {};
    let obj = [];
    let fee = {};
    let time = {};
    let min = 0;
    
    // 배열 순서
    for (let i = 0; i < records.length; i++) {
        arr[records[i].split(' ')[1]] = 0;
    }
    arr = Object.keys(arr).sort()



    // 초기화
    for (let i = 0; i < arr.length; i++) {
        fee[arr[i]] = 0;
        time[arr[i]] = [];
    }

    obj.push(fee);
    console.log(Object.keys(obj[0]).sort().reduce(function (result, key) {
        result[key] = obj[key];
        return result;
      }, {}))

    // 입차 출차 만들기
    for (let i = 0; i < records.length; i++) {
        if (records[i].split(' ')[2] === 'IN' || records[i].split(' ')[2] === 'OUT') {
            time[records[i].split(' ')[1]].push(records[i].split(' ')[0]);
        }
    }

    // 마지막 출차 없는 경우
    for (let key in time) {
        if (time[key].length % 2 === 1) {
            time[key].push("23:59");
        }
    }


    for (let key in time) {
        for (let i = 1; i < time[key].length; i+=2) {
            if (Number(time[key][i].split(':')[1]) < Number(time[key][i - 1].split(':')[1])) {
                // minute
                min += Number(time[key][i].split(':')[1]) + 60 - Number(time[key][i - 1].split(':')[1]);
                
                // hour
                min += (Number(time[key][i].split(':')[0]) - 1 - Number(time[key][i - 1].split(':')[0])) * 60;
            } else {
                // minute
                min += Number(time[key][i].split(':')[1]) - Number(time[key][i - 1].split(':')[1]);
                // hour
                min += (Number(time[key][i].split(':')[0]) - Number(time[key][i - 1].split(':')[0])) * 60;
            }
        }

        fee[key] = min
        min = 0;
    }

    for (let key in fee) {
        answer.push(money(fees, fee[key]));
    }
    
    return answer;
}




let fees = [120, 0, 60, 591];
let records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"];
console.log(solution(fees, records));