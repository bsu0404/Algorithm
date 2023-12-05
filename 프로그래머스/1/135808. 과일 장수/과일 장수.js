function solution(k, m, score) {
    var answer = 0;
    score.sort(function(a,b){
        return b-a;
    });
    // console.log(score);
    var tmp=0;
    while(score.length>=tmp+m){
        answer += score[tmp+m-1]*m;
        // console.log(answer + " "+score[tmp+m-1]);
        
        tmp=tmp+m;
    }
    return answer;
}