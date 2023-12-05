function solution(absolutes, signs) {
    var answer = 0;
    for (var i =0;i<absolutes.length;i++){
        var tmp = signs[i] ==true? 1*absolutes[i]:-1*absolutes[i];
        answer+=tmp;
    }
    return answer;
}