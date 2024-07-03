const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let [len, N] = input[0].split(" ").map(Number);

let alphabets = input[1].split(" ");
alphabets.sort();

let array = ["a", "e", "i", "o", "u"];

//dfs
function dfs(arr, vowel, consonant) {
  //모음 자음

  if (arr.length == len && vowel >= 1 && consonant >= 2) {
    console.log(arr.join(""));
    return;
  }
  for (let i = 0; i < alphabets.length; i++) {
    let alphabet = alphabets[i];
    if (arr.indexOf(alphabet) != -1 || arr[arr.length - 1] > alphabet) {
      //중복이면 , 오름차순이 아니면
      continue;
    }
 
    array.indexOf(alphabet) != -1
      ? dfs([...arr, alphabet], vowel + 1, consonant)
      : dfs([...arr, alphabet], vowel, consonant + 1);
  }
}

dfs([], 0, 0);