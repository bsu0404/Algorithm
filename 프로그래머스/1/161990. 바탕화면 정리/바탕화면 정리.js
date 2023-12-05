function solution(wallpaper) {
    var answer = [];
    answer=[Infinity,Infinity,-Infinity,-Infinity];
    for (var i = 0; i<wallpaper.length;i++){
        for (var j=0;j<wallpaper[i].length;j++){
            if (wallpaper[i][j]=="#"){              
                answer[0]=Math.min(answer[0],i);
                answer[1]=Math.min(answer[1],j);
                answer[2]=Math.max(answer[2],i);
                answer[3]=Math.max(answer[3],j);   
            }
        }
        
    }
    answer[2]+=1;
    answer[3]+=1;
    return answer;
}