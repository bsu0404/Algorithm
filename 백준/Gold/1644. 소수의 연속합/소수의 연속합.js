const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let N = fs.readFileSync(filePath).toString();
max = parseInt(N);

let array = new Array(max + 1).fill(0);
let primes = [];
const findPrime = () => {
  for (let i = 2; i <= max; i++) {
    let j = 2;
    while (i * j <= max) {
      array[i * j]++;
      j++;
    }
  }
  for (let i = 2; i <= max; i++) {
    if (array[i] == 0) {
      primes.push(i);
    }
  }

};
const cal_count = () => {
  let left = 0;
  let right = 0;
  let count = 0;
  let sum = 0;
  while (true) {
    if (left >= primes.length && right >= primes.length) {
      break;
    }
    if (sum == N) {
      count++;
      sum = sum - primes[left];

      left++;
    } else if (sum < N) {
      sum = sum + primes[right];
      right++;
    } else {
      sum = sum - primes[left];
      left++;
    }
    
  }
  console.log(count);
};
findPrime();
cal_count();

