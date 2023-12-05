function solution(keymap, targets) {
    var answer = [];
    for (var i = 0;i<targets.length;i++){
        answer[i]=0;
        for (var j=0;j<targets[i].length;j++){
            var min = Infinity;
            for (var k=0;k<keymap.length;k++){
                var tmp = keymap[k].indexOf(targets[i][j]);
                if(min>tmp&&tmp!=-1){
                    min=tmp+1;
                }
            }
            answer[i]=answer[i]+min;
        }
        if(answer[i]==Infinity){
            answer[i]=-1;
        }
    } 
    return answer;
}