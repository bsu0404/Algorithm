function solution(N, stages) {
    var answer = [];
    for(var i =0;i<N+1;i++){
        answer.push({index:i+1,fail:0,challenge:0});
    }
    for(var i =0;i<stages.length;i++){        
        answer[stages[i]-1].fail++;
    }
     for(var i =1;i<N;i++){
        answer[i].challenge=answer[i-1].challenge+answer[i-1].fail;
        
    }
    
    

    answer.sort(function(a,b){
       return b.fail/(stages.length-b.challenge)-a.fail/(stages.length-a.challenge);
    });
    var sortedAnswer=[];
    for(var i =0;i<N+1;i++){
        if(answer[i].index!=N+1)
        sortedAnswer.push(answer[i].index);
    }
    
    return sortedAnswer;
}