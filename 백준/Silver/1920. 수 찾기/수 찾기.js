const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

//방법1 set
let N = parseInt(input[0]);
let set1 = new Set(input[1].split(" ").map(Number));

let M = parseInt(input[2]);
let array = input[3].split(" ").map(Number);

let results = [];

results = array.map((num) => (set1.has(num) ? 1 : 0));
console.log(results.join("\n"));
