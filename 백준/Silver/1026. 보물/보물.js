const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let len = parseInt(input[0]);
let A = input[1].split(" ").map(Number);
let B = input[2].split(" ").map(Number);

A.sort((a, b) => a - b);
B.sort((a, b) => b - a);
let sum = 0;
for (let i = 0; i < len; i++) {
  sum = sum + A[i] * B[i];
}
console.log(sum);
