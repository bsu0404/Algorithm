function solution(k, score) {
    var answer = [];
    var honor = [];
    for (var i =0;i<score.length;i++){
        if (honor.length<k){
            honor.push(score[i]);
        }
        else{
            var min=Infinity;
            for (var j =0;j<k;j++){
                if (min>honor[j])
                    min=honor[j];
            }
            if (min<score[i]){
                honor[honor.indexOf(min)]=score[i];
            }
        }
         min=Infinity;
            for (var j =0;j<k;j++){
                if (min>honor[j])
                    min=honor[j];
            }
        answer[i]=min;
    }
    return answer;
}