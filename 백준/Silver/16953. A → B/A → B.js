const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let [goal, num] = fs.readFileSync(filePath).toString().split(" ").map(Number);

let count = 0;
while (goal < num) {
  if (num % 10 == 1) {
    num = parseInt(num / 10);
  } else if (num % 2 == 0) {
    num /= 2;
  } else {
    break;
  }
  count++;
}
console.log(num == goal ? count + 1 : -1);
