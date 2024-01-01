const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

//input 정리
let array =[];
for(let  i =0;i<input.length-1;i++){
    array.push(input[i].split(" ").slice(1));
    for(let j=0;j<array[i].length;j++){
        array[i][j]=(parseInt(array[i][j]));
    }
}
//dfs
function dfs(arr,num) {
    if (arr.length == 6) {
      console.log(arr.join(" "));
    } 
      for (let i = 0; i < array[num].length; i++) {
        let number = array[num][i];
        if (arr.indexOf(number) != -1 ||(arr[arr.length-1]>number) ) { //중복이면 , 오름차순이 아니면
          continue;
        }
        dfs([...arr, number],num); 
      }
 
  }
//로또 번호 case
  for (let i =0;i<array.length;i++){
    dfs([],i)
    console.log();
  }
