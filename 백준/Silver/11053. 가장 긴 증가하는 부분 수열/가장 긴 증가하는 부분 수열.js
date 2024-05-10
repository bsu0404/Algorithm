const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
input[0] = parseInt(input[0]);

input[1] = input[1].split(" ");
let dp = [];

for (let i = 0; i < input[1].length; i++) {
  dp[i] = [parseInt(input[1][i]), 1];
}
for (let i = 0; i < dp.length; i++) {
  for (let j = 0; j < i; j++) {
    if (dp[j][0] < dp[i][0] && dp[j][1] >= dp[i][1]) {
      dp[i][1] = dp[j][1] + 1;
    }
  }
}
for (let i = 0; i < dp.length; i++) {
  dp[i] = dp[i][1];
}

console.log(Math.max(...dp));
