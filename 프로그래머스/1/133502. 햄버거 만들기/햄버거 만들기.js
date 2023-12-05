function solution(ingredient) {
    var answer = 0;
    var str = [];
    for (var i =0;i<ingredient.length;i++){
        str.push(ingredient[i]);

        if(str.slice(-4).join("")=="1231"){
            answer++;
            // str=str.slice(0,-4);
            str.pop();
            str.pop();
            str.pop();
            str.pop();
            
        }
    
    }
    
    return answer;
}