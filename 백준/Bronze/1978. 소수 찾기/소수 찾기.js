const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let len = parseInt(input[0]);

let arr = input[1].split(" ").map(Number);

arr.sort((a, b) => a - b);
let count = 0;

function isPrime(num) {
  if (num == 1) {
    return false;
  }
  for (let j = 2; j <= Math.sqrt(num); j++) {
    if (num % j == 0) {
      return false;
    }
  }
  return true;
}

for (let i = 0; i < len; i++) {
  if (isPrime(arr[i])) {
    count++;
  }
}

console.log(count);
