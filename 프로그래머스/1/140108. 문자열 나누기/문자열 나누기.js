function solution(s) {
    var answer = 0;
    var tmp ="";
    var same=0;
    var diff=0;
    for (var i = 0;i<s.length;i++){
        if (tmp==""){
            tmp=s[i];
            same++;
        }
        else if(tmp==s[i]){
            same++;
            if(same==diff){
                tmp=""
                answer++;              
            }
        }
        else{
            diff++;
            if(same==diff){
                tmp=""
                answer++;                
            }
        }
    }
    if (same!=diff){
        answer++;
    } 
    return answer;
}