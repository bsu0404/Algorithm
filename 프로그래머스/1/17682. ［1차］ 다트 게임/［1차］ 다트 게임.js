function solution(dartResult) {
    var answer = [0,0,0];
    var num=-1;
    for (var i=0;i<dartResult.length;i++){
        if(dartResult[i]=="S"){
            answer[num]=answer[num]**1;
        }
        else if(dartResult[i]=="D"){
            answer[num]=answer[num]**2;
        }
        else if(dartResult[i]=="T"){
            answer[num]=answer[num]**3;
        }
        else if(dartResult[i]=="*"){
            answer[num]=answer[num]*2;
            if(num-1>=0){
                answer[num-1]=answer[num-1]*2;
            }
        }
        else if(dartResult[i]=="#"){
            answer[num]=answer[num]*(-1);
        }
        else{ //숫자인 경우
            if (dartResult[i-1]>="0"&&dartResult[i-1]<="9"){
                answer[num]=answer[num]*10+parseInt(dartResult[i]);
            }
            
            else{
            num++;
                
            answer[num]=parseInt(dartResult[i]);
                
            }
            console.log(num+ " "+ dartResult[i]);
        }   
        
        
    }
    return answer[0]+answer[1]+answer[2];
}