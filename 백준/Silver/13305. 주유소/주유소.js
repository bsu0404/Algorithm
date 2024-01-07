const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let N = parseInt(input[0]);
let len = input[1].split(" ").map(BigInt);
let costs = input[2].split(" ").map(BigInt);
let sum = BigInt(0);
let min = BigInt(costs[0]);
let current_len = BigInt(0);

for (let i = 0; i < costs.length; i++) {
  let cost = costs[i];
    if (cost < min || i == N - 1) {
    sum = sum + current_len * min;
    min = cost;
    current_len = BigInt(0);
  }
  if (i != N - 1) current_len = current_len + BigInt(len[i]);
}
console.log(sum.toString());