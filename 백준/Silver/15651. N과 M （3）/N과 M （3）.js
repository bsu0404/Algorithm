//return 필요.
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split(" ");

let answer ='';
for (let i = 0; i < input.length; i++) {
  input[i] = parseInt(input[i]);
}

function dfs(arr) {
  if (arr.length == input[1]) {
    answer = answer.concat(arr.join(" ")+"\n")
    return;
  } 
    for (let i = 1; i <= input[0]; i++) {     
      // dfs([...arr, i]); 
        arr.push(i)
        dfs(arr);
        arr.pop()
    }
  
}
dfs([]);

console.log(answer);