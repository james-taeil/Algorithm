const solution = (land) => {
    let len = land.length;
    
    // 처음은 DFS로 생각하였으나, 재귀를 생각하면 100000개가 있을 경우 시간 초과 예상
    // 결론은 DP밖에 없을 것 같다.

    //! 마지막 행에서 그 전에 행에게 자신의 열을 제외한 숫자 중 최대값을 누적으로 합해준다.
    //* 핵심은 최대값을 어떻게 넘겨줄 것인가? 라는 문제
    for(let i = len - 2; i >= 0; i--) {
        land[i][0] = Math.max(land[i + 1][1], land[i + 1][2], land[i + 1][3]) + land[i][0];
        land[i][1] = Math.max(land[i + 1][0], land[i + 1][2], land[i + 1][3]) + land[i][1];
        land[i][2] = Math.max(land[i + 1][0], land[i + 1][1], land[i + 1][3]) + land[i][2];
        land[i][3] = Math.max(land[i + 1][0], land[i + 1][1], land[i + 1][2]) + land[i][3];
    }

    return Math.max(...land[0]);
}

let land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]];
console.log(solution(land));