const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim();
let [a, b] = input.split(" ").map(Number);

b = Math.min(10000000, b);
const isPalindrome = (num) => {
  const number = num.toString();
  for (let i = 0, j = number.length - 1; i < j; i++, j--) {
    if (number[i] !== number[j]) {
      return false;
    }
  }
  return true;
};

function isPrime(num) {
  for (let j = 2; j <= Math.sqrt(num); j++) {
    if (num % j == 0) {
      return false;
    }
  }
  return true;
}
let results = [];
for (let i = a; i <= b; i++) {
  if (i != 11 && i.toString().length % 2 == 0) {
    continue;
  }
  if (isPalindrome(i) && isPrime(i)) {
    results.push(i);
  }
}
results.push(-1);

console.log(results.join("\n"));
