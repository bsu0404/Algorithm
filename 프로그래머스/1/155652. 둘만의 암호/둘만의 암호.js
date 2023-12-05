function solution(s, skip, index) {
    var answer = '';
    skip=skip.split('');
    for(var i=0;i<skip.length;i++){
        skip[i]=(skip[i].charCodeAt()-97)%26;// a는 0, b는 1 ... 저장
    }
    console.log(skip);
    s=s.split('');
    for (var i=0;i<s.length;i++){
     var sum=index;
     for (var j=1;j<=sum;j++){
        if(skip.indexOf((s[i].charCodeAt()-97+j)%26)!=-1){ //더한게 몇번째인지
            sum++; //겹친다면 하나 더 더함
        }
     }
        s[i]=(97+(s[i].charCodeAt()-97+sum)%26);
        s[i]=String.fromCharCode(s[i]);
       
    }
    answer=s.join('');
    return answer;
}