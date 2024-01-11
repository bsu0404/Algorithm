const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n").map(Number);

let N = input[0];
let array = input.slice(1);

let results = [];
for (let i = 0; i < N; i++) {
  let num = array[i];
  let min = [-Infinity, Infinity];
  for (let j = 0; j <= num / 2; j++) {
    if (num - j < Math.abs(min[1], min[0])) {
      if (isPrime(j) && isPrime(num - j)) {
        min[0] = j;
        min[1] = num - j;
      }
    }
  }
  results.push(min);
}
results.forEach((num) => console.log(num.join(" ")));

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
