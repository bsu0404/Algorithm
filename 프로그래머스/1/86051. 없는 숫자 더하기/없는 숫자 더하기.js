function solution(numbers) {
    var answer = 0;
    for (var i =0;i<=9;i++){
        if (numbers.indexOf(i)==-1){
            answer+=i;
        }
    }
    return answer;
}