function solution(a, b, n) {
    var answer = 0;
    while(n>=a){
        answer+=Math.floor(n/a)*b;
        console.log("answer "+answer);
        n=n%a+Math.floor(n/a)*b; 
        console.log("n "+n);
    }
    return answer;
}