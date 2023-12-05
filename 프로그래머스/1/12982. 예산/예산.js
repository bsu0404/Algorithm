function solution(d, budget) {
    var answer = 0;
    d.sort(function(a,b){
        return a-b;
    })
    var sum =0;
    for (var i=0;i<d.length;i++){
        sum+=d[i];
        if(sum>budget){
            break;
        }
    }
    return i;
}