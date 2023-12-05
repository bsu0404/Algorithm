function solution(s) {
    var answer = [];
    for (var i = s.length-1; i>0;i--){
        var j=i-1;
        while(s[j]!=s[i]&&j!=-1){
            j--;
        }
        if(j==-1)
        answer.unshift(j);
        else
            {
        answer.unshift(i-j);
                
            }
    }
    answer.unshift(-1);
    return answer;
}