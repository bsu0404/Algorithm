const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let N = parseInt(input[0]);
let len = input[1].split(" ").map(Number);
let costs = input[2].split(" ").map(Number);
let sum = 0;
let min = costs[0];
let current_len = 0;

for (let i = 0; i < costs.length; i++) {
  let cost = costs[i];
  
  if (cost < min || i == N - 1) {
    sum = sum + current_len * min;
    min = cost;
    current_len = 0;
  }
  current_len = current_len + len[i];
}
console.log(sum);
