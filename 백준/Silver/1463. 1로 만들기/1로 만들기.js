const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString();
input = parseInt(input);

dp = [0, 0, 1, 1];
let answer = Infinity;
let a, b, c;
for (let i = 4; i <= input; i++) {
  a = Number.isInteger(i / 2) ? dp[i / 2] : Infinity;
  b = Number.isInteger(i / 3) ? dp[i / 3] : Infinity;
  c = dp[i - 1];
  dp[i] = Math.min(a, b, c) + 1;
}

console.log(dp[input]);
