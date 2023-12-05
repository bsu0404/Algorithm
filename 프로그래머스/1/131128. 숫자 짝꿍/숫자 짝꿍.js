function solution(X, Y) {
    var answer = '';
    var numbers=[];
    X=X.split("");
    X.sort(function(a,b){
            return a-b;
    });
    Y=Y.split("");
    Y.sort(function(a,b){
            return a-b;
    });
    var j =0;
    var i =0;
    while(i<X.length&&j<Y.length){       
        if(Y[j]==X[i]){
            numbers.push(Y[j]);         
            i++;
            j++;
        }
        else if(X[i]>Y[j]){
            j++
        }
        else if(Y[j]>X[i]){
            i++;
        }      
    }
    
    
    if (numbers.length==0){
        return "-1";
    }
    else{
        numbers.sort(function(a,b){
            return b-a;
        });
        numbers=numbers.join("");
        if (numbers[0]==0)
            numbers = "0";   
    }
    return numbers;
}