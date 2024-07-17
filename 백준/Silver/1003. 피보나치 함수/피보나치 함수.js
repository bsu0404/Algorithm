const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let max_num = Math.max(...input.slice(1));
let dp = [
  [1, 0],
  [0, 1],
  [1, 1],
];
for (let i = 3; i <= max_num; i++) {
  let tmp = [];
  tmp[0] = dp[i - 1][0] + dp[i - 2][0];
  tmp[1] = dp[i - 1][1] + dp[i - 2][1];
  dp[i] = tmp;
}
for (let i = 1; i <= input[0]; i++) {
  let tmp = dp[parseInt(input[i])];
  console.log(`${tmp[0]} ${tmp[1]}`);
}