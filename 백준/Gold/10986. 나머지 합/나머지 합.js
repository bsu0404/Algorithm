const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number);
let array = input[1].split(" ").map(Number);

let quotient = Array(M).fill(0);
quotient[0] = 1;
let sum = [0];

for (let i = 1; i <= N; i++) {
  sum.push(sum[i - 1] + array[i - 1]);
  quotient[sum[i] % M]++;
}
let result = 0;
for (let i = 0; i < M; i++) {
  result += (quotient[i] * (quotient[i] - 1)) / 2;
}
console.log(result);
