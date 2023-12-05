function solution(babbling) {
    var answer = 0;
    var words =["aya","ye","woo","ma"]; //만들 수 있는걸 다 만들고 ->절대 안됨
    console.log((babbling[0]));
    
    for (var i =0; i<babbling.length;i++){
        var tmp=0;
        for (var j=0;j<4;j++){
            babbling[i]=babbling[i].replace(new RegExp(words[j], 'g'), j);   
        }
    console.log("정규화 결과: "+(babbling[i]));
        
        for (var j = 0;j<babbling[i].length;j++){
           if ("0"<=babbling[i][j]&&babbling[i][j]<="4"){
               if (babbling[i][j]==babbling[i][j-1]){ //반복된 경우 break
                    break;
                }
           }
           else{
               break; //1-4로 정규화되지 않은 경우 break
           }
            if(j==babbling[i].length-1) { //break되지 않고 마지막까지 통과한 경우
                answer++; 
            }
        }    
    }
    

   

    return answer;
}