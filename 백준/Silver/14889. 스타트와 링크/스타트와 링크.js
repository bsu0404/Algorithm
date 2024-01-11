const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

//input 정리
let len = parseInt(input[0]);
let array = input.slice(1);
for (let i = 0; i < len; i++) {
  array[i] = array[i].split(" ").map(Number);
}
//초기화
let min = Infinity;
let visited = new Array(len).fill(0);

//능력치 차이 계산
function cal_abs() {
  let a = 0;
  let b = 0;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (visited[i] == 1 && visited[j] == 1) {
        a = a + array[i][j];
      } else if (visited[i] == 0 && visited[j] == 0) {
        b = b + array[i][j];
      }
    }
  }
  min = Math.min(min, Math.abs(a - b));
  return;
}

//dfs
function dfs(idx, count) {
  if (count == len / 2) {
    cal_abs();
    return;
  }

  for (let i = idx; i < len; i++) {
    if (visited[i] == 0) {
      visited[i] = 1;
      dfs(i + 1, count + 1);
      visited[i] = 0;
    }
  }
}

dfs(0, 0);

console.log(min);
