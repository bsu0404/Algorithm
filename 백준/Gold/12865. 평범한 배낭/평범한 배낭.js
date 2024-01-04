const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
//input 정리
input[0] = input[0].split(" ");
let len = parseInt(input[0][0]);
let goal = parseInt(input[0][1]);
//초기화
let array = [];
let dp = Array.from({ length: len + 1 }, () => new Array(goal + 1).fill(0));
for (let i = 1; i <= len; i++) {
  input[i] = input[i].split(" ");
  array.push([parseInt(input[i][0]), parseInt(input[i][1])]);
}
//dp구하기
for (let i = 1; i < len + 1; i++) {
  for (let j = 1; j < goal + 1; j++) {
    let weight = array[i - 1][0]; //무게
    let value = array[i - 1][1]; //가치
    if (j >= weight) {
      //
      dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight] + value);
    } else {
      //이전 물건까지 사용했을 때 최댓값
      dp[i][j] = dp[i - 1][j];
    }
  }
}
console.log(dp[len][goal]);
