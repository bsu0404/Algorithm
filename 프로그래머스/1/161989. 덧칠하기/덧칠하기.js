function solution(n, m, section) {
    var answer = 1;
    var tmp=0;
    for (var i = 1; i<section.length;i++){     
        
            if(section[i]-section[tmp]<m){                
            }
            else{
                answer++;
                tmp=i;
            }
        
        
    }
    return answer;
}