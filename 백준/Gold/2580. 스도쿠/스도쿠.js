const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let sudoku = [];
for (let i = 0; i < input.length; i++) {
  sudoku.push(input[i].split(" ").map(Number));
}

let zeros = [];
for (let i = 0; i < input.length; i++) {
  for (let j = 0; j < 9; j++) {
    if (sudoku[i][j] == 0) {
      zeros.push([i, j]);
    }
  }
}

function isOk(a, b, k) {
  for (let i = 0; i < 9; i++) {
    let num = sudoku[a][i];
    if (num == k) {
      return false;
    }
  }

  for (let i = 0; i < 9; i++) {
    let num = sudoku[i][b];
    if (num == k) {
      return false;
    }
  }

  for (let i = parseInt(a / 3) * 3; i < parseInt(a / 3) * 3 + 3; i++) {
    for (let j = parseInt(b / 3) * 3; j < parseInt(b / 3) * 3 + 3; j++) {
      num = sudoku[i][j];
      if (num == k) {
        return false;
      }
    }
  }
  return true;
}

function dfs(index) {
  if (index == zeros.length) {
    for (let i = 0; i < 9; i++) {
      console.log(sudoku[i].join(" "));
    }
    process.exit();
  }

  for (let k = 1; k < 10; k++) {
    let i = zeros[index][0];
    let j = zeros[index][1];
    if (isOk(i, j, k)) {
      sudoku[i][j] = k;
      dfs(index + 1);
      sudoku[i][j] = 0;
    }
  }
}

dfs(0);
