const sdoku = (n) => {
  // let board = Array.from(Array(n), () => Array(n).fill(0));
  let board = [
    [1, 4, 3, 6, 2, 8, 5, 7, 9],
    [5, 7, 2, 1, 3, 9, 4, 7, 8],
    [9, 8, 6, 7, 5, 4, 2, 3, 1],
    [3, 9, 1, 5, 4, 2, 7, 8, 6],
    [4, 6, 8, 9, 1, 7, 3, 5, 2],
    [7, 2, 5, 8, 6, 3, 9, 1, 4],
    [2, 3, 7, 4, 8, 1, 6, 9, 5],
    [6, 1, 9, 2, 7, 5, 8, 4, 3],
    [8, 5, 4, 3, 9, 6, 1, 2, 7]
  ]
  
  const check = (board, n) => {
    for (let i = 0; i < n; i++) {
      let row = Array.from(Array(n).fill(0));
      let col = Array.from(Array(n).fill(0));

      for (let j = 0; j < n; j++) {
        row[board[i][j]] = 1;
        col[board[j][i]] = 1;

        if (row.reduce((a, c) => a + c) !== 9 || col.reduce((a, c) => a + c) !== 9) return false;
          
      }
    }

    // box check
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        let box = Array.from(Array(n).fill(0));
        for (let k = 0; k < 3; k++) {
          for (let s = 0; s < 3; s++) {
            box[board[i * 3 + k][j + 3 + s]] = 1;
          }
        }
        if (box.reduce((a, c) => a + c) !== 9) return false;
      }
    }
    return true;
  }

  return check(board, n);
}

let n = 9;
console.log(sdoku(n));