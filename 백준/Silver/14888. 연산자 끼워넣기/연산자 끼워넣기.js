const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
//input 정리
let len = parseInt(input[0]); // 숫자 수
let nums = input[1].split(" ").map(Number);
let operator = input[2].split(" ").map(Number);

let max = -Infinity;
let min = Infinity;
function cal(num1, num2, op) {
  if (op == 0) {
    return num1 + num2;
  }
  if (op == 1) {
    return num1 - num2;
  }
  if (op == 2) {
    return num1 * num2;
  }
  if (op == 3) {
    return parseInt(num1 / num2);
  }
}

function dfs(idx, sum) {
  if (idx == len) {
    max = Math.max(max, sum);
    min = Math.min(min, sum);
  }
  for (let i = 0; i < operator.length; i++) {
    if (operator[i] == 0) {
      continue;
    }
    operator[i] -= 1;

    dfs(idx + 1, cal(sum, nums[idx], i));
    operator[i] += 1;
  }
}

dfs(1, nums[0]);

console.log(max ? max : 0);
console.log(min ? min : 0);
