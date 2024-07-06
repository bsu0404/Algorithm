const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

input[0] = input[0].split(" ");
let len = parseInt(input[0][0]);
let num = parseInt(input[0][1]);

let array = [];

for (let i = 1; i < input.length; i++) {
  array.push(parseInt(input[i]));
}

array.reverse();
let count = 0;
while (num > 0) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] <= num) {
      //console.log(array[i]);
      let quotient = parseInt(num / array[i]);
      num = num - array[i] * quotient;
      count = count + quotient;
      //console.log(`count: ${count} num: ${num} array[i]: ${array[i]}`);
    }
  }
}
console.log(count);
