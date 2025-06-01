const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let dp = [0, 1, 2, 4];
let max_num = Math.max(...input.slice(1));

for (let i = 4; i <= max_num; i++) {
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
}

for (let i = 1; i <= input[0]; i++) {
  console.log(dp[parseInt(input[i])]);
}
