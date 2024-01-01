const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
//input 정리
let len = parseInt(input[0]);
let array =[]
for (let i=1;i<=len;i++){
    input[i]=input[i].split(" ");
    for(let j=0;j<input[i].length;j++){
        input[i][j]=parseInt(input[i][j]);
    }
    array.push(input[i]);
}
//초기화 
const dp = Array.from({ length: len }, () => Array(3).fill(0));
  
dp[0][0]=array[0][0];
dp[0][1]=array[0][1];
dp[0][2]=array[0][2];

//dp채우기- dp에 들어가는 값: i번째에서 해당 색상 골랐을 때 최소
for (let i=1;i<len;i++){
    dp[i][0] = array[i][0] +Math.min(dp[i-1][1],dp[i-1][2]);
    dp[i][1] = array[i][1] +Math.min(dp[i-1][0],dp[i-1][2]);
    dp[i][2] = array[i][2] +Math.min(dp[i-1][0],dp[i-1][1]);    
}

//최소 출력
console.log(Math.min(...dp[len-1]))
