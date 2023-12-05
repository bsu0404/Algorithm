function solution(number, limit, power) {
    var answer = 0;
    var numbers = Array(number+1).fill(0);
    
    console.log(numbers);
    for (var i=1;i<=number;i++){ //주어진 숫자까지 돌아감
        var j=0; //초기는 0
        while(j<=number){ //i의 배수에 1씩 더함.    
            numbers[j]++;
            j=j+i; //i의 배수를 찾기 위해 i를 더함
        }
        
    }
    console.log(numbers);
    
   for (var i=1;i<=number;i++){
       if(numbers[i]<=limit){
            answer+=numbers[i];    
       }
       else{
           answer+=power;
       }
   }
    return answer;
}