const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let N = parseInt(input[0]);
let len = input[1].split(" ").map(Number);
let cost = input[2]
  .split(" ")
  .map(Number)
  .slice(0, N - 1);

let sum = 0;
let sub = 0;

for (let i = len.length - 2; i >= 0; i--) {
  len[i] += len[i + 1];
}

while (cost.length > 0) {
  let min = Math.min(...cost);
  let index = cost.indexOf(min);
  cost = cost.slice(0, index);

  let add = min * (len[index] - sub);

  sum = sum + add;
  sub = sub + len[index];
}
console.log(sum);
