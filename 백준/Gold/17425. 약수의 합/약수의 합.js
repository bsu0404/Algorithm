const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let array = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);
//input
let n = array.shift();
let max = 1000001;
let results = [];
let dp = new Array(max).fill(1);
const f = () => {
  //dp[i] : i를 만드는 약수의 합
  for (let i = 2; i < max; i++) {
    let j = 1;
    while (i * j < max) {
      dp[i * j] += i;
      j++;
    }
  }
};

f();

for (let i = 2; i < max; i++) {
  dp[i] += dp[i - 1];
}
array.forEach((num) => {
  // results = results + dp[num].toString() + "\n";
  results.push(dp[num]);
});
// console.log(results);
console.log(results.join("\n"));

