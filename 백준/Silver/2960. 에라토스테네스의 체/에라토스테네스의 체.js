const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let [N, K] = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let numbers = new Set();

for (let i = 1; i <= N; i++) {
  numbers.add(i);
}
let count = 0;

for (let i = 2; i <= N; i++) {
  if (isPrime(i)) {
    let target = i;
    while (target <= N) {
      if (numbers.delete(target)) {
        if (++count == K) {
          console.log(target);
          process.exit();
        }
      }
      target = target + i;
    }
  }
}

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
