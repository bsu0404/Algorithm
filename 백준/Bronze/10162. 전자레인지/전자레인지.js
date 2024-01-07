const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
input = parseInt(input);

let times = [300, 60, 10];
let count = [];
for (let time of times) {
  quotient = parseInt(input / time);
  input = input - time * quotient;
  count.push(quotient);
}
console.log(input ? -1 : count.join(" "));