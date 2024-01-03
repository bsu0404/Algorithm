const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let len = parseInt(input[0]);
let array = input[1].split(" ");
for (let i = 0; i < len; i++) {
  array[i] = parseInt(array[i]);
}
let dp1 = new Array(len).fill(1);
let dp2 = new Array(len).fill(1);

//앞에서부터 증가하는 수열
for (let i = 0; i < len; i++) {
  for (let j = 0; j < i; j++) {
    if (array[i] > array[j]) {
      dp1[i] = Math.max(dp1[j] + 1, dp1[i]);
    }
  }
}
//뒤에서부터 증가하는 수열
array.reverse();
for (let i = 0; i < len; i++) {
  for (let j = 0; j < i; j++) {
    if (array[i] > array[j]) {
      dp2[i] = Math.max(dp2[j] + 1, dp2[i]);
    }
  }
}
dp2.reverse();
//최대 구하기
let max = 0;
for (let i = 0; i < len; i++) {
  max = Math.max(max, dp1[i] + dp2[i]);
}

console.log(max - 1);
