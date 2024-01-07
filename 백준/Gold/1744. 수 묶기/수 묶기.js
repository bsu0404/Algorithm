const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let len = parseInt(input[0]);
let array = input
  .slice(1)
  .map(Number)
  .sort((a, b) => a - b);
let sum = 0;
let i = 0;

//음수,0
while (array[i] <= 0) {
  if (array[i + 1] <= 0) {
    //[음수,음수(0)]
    sum = sum + array[i] * array[i + 1];
    i += 2;
  } else {
    //[음수(0),양수] - 마지막 음수
    sum = sum + array[i];
    i++;
  }
}

array = array.slice(i);
array.reverse();
i = 0;

//양수
while (array[i]) {
  if (!array[i + 1]) {
    //마지막 숫자 1개
    sum = sum + array[i];
    i++;
    break;
  } else {
    if (array[i + 1] == 1) {
      sum = sum + array[i];
      i++;
    } else {
      sum = sum + array[i] * array[i + 1];
      i += 2;
    }
  }
}

console.log(sum);
