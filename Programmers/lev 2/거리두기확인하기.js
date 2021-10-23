// const isRange = (x, y) => {
//   let size = 5;
//   return 0 <= x && x < size && 0 <= y && y < size;
// }

// const isCheck = (r, c, p) => {
//   // 남동북서 한칸씩
//   let dist, nx, ny;
//   dist = [[1, 0], [0, 1], [-1, 0], [0, -1]];
//   for (let [dx, dy] of dist) {
//     nx = r + dx;
//     ny = c + dy;
//     if (isRange(nx, ny) && p[nx][ny] === 'P') return false;
//   }

//   // 대각선 한칸씩
//   dist = [[1, 1], [-1, 1], [1, -1], [-1, -1]];
//   for (let [dx, dy] of dist) {
//     nx = r + dx;
//     ny = c + dy;
//     if (isRange(nx, ny) && p[nx][ny] === 'P' && (p[r][ny] !== "X" && p[nx][c] !== "X")) {
//       return false;
//     }
//   }

//   // 남동북서 두칸씩
//   dist = [[2, 0], [0, 2], [-2, 0], [0, -2]];
//   for (let [dx, dy] of dist) {
//     nx = r + dx;
//     ny = c + dy;
//     if (isRange(nx, ny) && p[nx][ny] === 'P' && p[r + dx / 2][c + dy / 2] !== "X") {
//       return false;
//     }
//     return true;
//   }

// }

// const solution = (places) => {
//   let answer = [];
//   let matrix = [];
//   for (let i = 0; i < places.length; i++) {
//     for (let j = 0; j < places.length; j++) {
//       matrix.push([i, j]);
//     }
//   }

//   for (let place of places) {
//     for (let [row, col] of matrix) {
//       if (place[row][col] === 'P' && (!isCheck(row, col, place))) {
//         answer.push(0);
//         break;
//       } else {
//         answer.push(1);
//       }
//     }
//   }
//   return answer;
// }

// const BFS = (dx, dy, people, place) => {
//   let visited = [];
//   for (let i = 0; i < 5; i++) {
//     visited.push(new Array(5).fill(false));
//   }
//   let count = 0;
//   let arr = [];
//   arr.push(people);
  
//   while (arr) {
//     for (let el of arr) {
//       let [y, x] = arr.shift();
//       for (let i = 0; i < 4; i++) {
//         nx = x + dx[i];
//         ny = y + dy[i];

//         if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5 || visited[ny][nx]) {
//           continue;
//         }
//         if (place[ny][nx] === 'P') {
//           return false;
//         } else if (place[ny][nx] === 'X') {
//           continue;
//         } else {
//           arr.push([ny, nx])
//         }
//       }
//     }

//     count += 1;
//     if (count === 2 || !arr) {
//       return true;
//     }
//   }

// }

// const solution = (places) => {
//   let answer = [];
//   for (let place of places) {
//     let peoples = [];
//     for (let i = 0; i < 5; i < i++) {
//       for (let j = 0; j < 5; j < j++) {
//         if (place[i][j] === 'P') {
//           peoples.push([i, j]);
//         }
//       }
//     }

//     if (peoples.length === 0) {
//       answer.push(1);
//     }
//     console.log(peoples)

//     let personCheck = true;
//     let dx = [-1, 1, 0, 0];
//     let dy = [0, 0, 1, -1];
//     for (let people of peoples) {
//       if (!BFS(dx, dy, people, place)) {
//         personCheck = false;
//         break;
//       }
//     }

//     if (!personCheck) {
//       answer.push(0);
//     } else {
//       answer.push(1);
//     }

//     return answer;
//   }
// }

const isRange = (x, y) => {
  let size = 5;
  return 0 <= x && x < size && 0 <= y && y < size;
}

const solution = (places) => {
  let answer = [];
  for (let place of places) {
    let flag = 0;
    console.log(place)
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        
        if (place[i][j] === "P") {
          if ((isRange(i + 1, j) && place[i + 1][j]) === "P") {
            flag = 1;
          }
          if ((isRange(i + 2, j) && place[i + 2][j]) === "P" && place[i + 1][j] !== 'X') {
            flag = 1;
          }
          if ((isRange(i, j + 1) && place[i][j + 1]) === "P") {
            flag = 1;
          } 
          if ((isRange(i, j + 2) && place[i][j + 2]) === "P" && place[i][j + 1] !== 'X') {
            flag = 1;
          }
          if ((isRange(i + 1, j + 1) && place[i + 1][j + 1]) === "P" && place[i + 1][j] !== 'X' && place[i][j + 1] !== 'X') {
            flag = 1;
          }
          if ((isRange(i + 1, j - 1) && place[i + 1][j - 1]) === "P" && place[i][j - 1] !== 'X' && place[i + 1][j] !== 'X') {
            flag = 1;
          }
        }
      }
    }
    if (flag !== 0) {
      answer.push(0);
    } else {
      answer.push(1);
    }
  }
  return answer;
}


// // 동 서 남 북
// const dX = [1, -1, 0, 0];
// const dY = [0, 0, 1, -1];

// // 좌료가 배열 내부인지 판단
// const inRange = (x, y) => {
//   return 0 <= x && x < 5 && 0 <= y && y < 5;
// };

// // 맨해튼 거리 계산
// const inDistance = (x1, y1, x2, y2) => {
//   return Math.abs(x1 - x2) + Math.abs(y1 - y2) <= 2 ? true : false;
// };

// const bfs = (place, visited) => {
//   let queue = [];

//   for (let startY = 0; startY < 5; startY++) {
//     for (let startX = 0; startX < 5; startX++) {
//       if (place[startY][startX] === "P") {
//         queue.push([startX, startY]); // 시작 기준 x, y 저장

//         while (queue.length) {
//           let [x, y] = queue.shift();
//           visited[y][x] = true;

//           for (let i = 0; i < 4; i++) {
//             const nX = x + dX[i];
//             const nY = y + dY[i];

//             if (
//               inRange(nX, nY) &&
//               inDistance(startX, startY, nX, nY) &&
//               !visited[nY][nX]
//             ) {
//               if (place[nY][nX] === "P") {
//                 return 0;
//               }
//               if (place[nY][nX] !== "X") {
//                 queue.push([nX, nY]);
//               }
//             }
//           }
//         }
//       }
//     }
//   }

//   return 1;
// };


// const solution = (places) => {
//   let answer = places.map(place => {
//     return place.some()
//   })
// }

let places = [
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
];
console.log(solution(places))
