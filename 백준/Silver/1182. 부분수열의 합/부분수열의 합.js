const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let answer = 0;
//input 정리
input[0] = input[0].split(" ");
let len = parseInt(input[0][0]);
let num = parseInt(input[0][1]);
let array = [];
input[1] = input[1].split(" ");
for (let i = 0; i < input[1].length; i++) {
  array.push(parseInt(input[1][i]));
}
//dfs
function dfs(idx, sum) {
  if (idx == len) {
    if (sum == num) {
      answer++;
    }
    return;
  }
  dfs(idx + 1, sum + array[idx]);
  dfs(idx + 1, sum);
}
dfs(0, 0);
//빈 배열인 경우
if (num == 0) {
  answer -= 1;
}
console.log(answer);
