function solution(name, yearning, photo) {
    var answer = [];
    
    for (var i =0;i<photo.length;i++){
   answer[i]=0;
        for (var j=0;j<photo[i].length;j++){
            if(name.indexOf(photo[i][j])!=-1)
            answer[i]+=yearning[name.indexOf(photo[i][j])];
        }
    }
    return answer;
}