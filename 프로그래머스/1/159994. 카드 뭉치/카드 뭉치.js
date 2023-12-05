function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    for(var i =0;i<goal.length;i++){
        if (goal[i]==cards1[0]||goal[i]==cards2[0]){
            if (goal[i]==cards1[0]){
                cards1.shift();
            }
            else{
                cards2.shift();
            }
        }
        else{
           
            return "No"
        }
    }
    return answer;
}