const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
//input 정리
input[0] = input[0].split(" ");
let len = parseInt(input[0][0]);
let goal = parseInt(input[0][1]);
let coins = [];
for (let i = 1; i <= len; i++) {
  coins.push(parseInt(input[i]));
}
//초기화
let dp = new Array(goal + 1).fill(-1);

for (let j = 0; j < len; j++) {
  let coin = coins[j];
  if (dp[coin]) {
    dp[coin] = 1;
  }
}
//dp 구하기
for (let i = 1; i < goal + 1; i++) {
  for (let j = 0; j < len; j++) {
    let coin = coins[j];
    let ref = dp[i - coin];
    if (ref != -1 && ref) {
      if (dp[i] == -1) {
        dp[i] = ref + 1;
      } else {
        dp[i] = Math.min(ref + 1, dp[i]);
      }
    }
  }
}
console.log(dp[goal]);
