const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let num = fs.readFileSync(filePath).toString();

let sum = 0;
let count = 1;

while (sum < num) {
  count++;
  sum += count;
}
console.log(count - 1);
