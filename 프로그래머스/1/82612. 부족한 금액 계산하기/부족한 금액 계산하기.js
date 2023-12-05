function solution(price, money, count) {
    var answer = 0;
    var sum=0;
    for (var i=1;i<=count;i++){
        sum+=price*i;
        
    }
    if(sum-money>0)
        answer = sum-money;
    else
        answer=0;
    return answer;
}