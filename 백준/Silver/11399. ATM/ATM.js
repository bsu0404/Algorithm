const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let len = parseInt(input[0]);
let array = input[1].split(" ").map(Number);

array.sort((a, b) => {
  return a - b;
});

let wait = 0;
let sum = 0;
for (let i = 0; i < array.length; i++) {
  wait += array[i];
  sum += wait;
}
console.log(sum);
