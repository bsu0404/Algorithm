const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let [M, N] = fs.readFileSync(filePath).toString().split(" ").map(Number);

let results = [];

for (let i = M; i <= N; i++) {
  if (isPrime(i)) {
    results.push(i);
  }
}
console.log(results.join("\n"));

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