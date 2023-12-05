function solution(food) {
    var answer = [0];

    for (var i = food.length-1;i>0;i--){
        var tmp="";
        for (var j=0;j<Math.floor(food[i]/2);j++){
             tmp=tmp+i.toString();     
        }
        answer.push(tmp);
        answer.unshift(tmp);
       
    }
    answer=answer.join("");
    return answer;
}