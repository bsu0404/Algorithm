const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n").map(Number);
let max = -Infinity;
let array = input.slice(1).sort((a, b) => b - a);
for (let i = 0; i < array.length; i++) {
  max = Math.max(max, array[i] * (i + 1));
}
console.log(max);
