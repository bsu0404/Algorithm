function solution(answers) {
    var answer = [0,0,0];
    var std1=[1,2,3,4,5];
    var std2=[2, 1, 2, 3, 2, 4, 2, 5];
    var std3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    //1번은 5개 반복, 2번은 8개, 3번은 10개
    for (var i =0; i<answers.length;i++){
        if (std1[i%5]==answers[i]){
            answer[0]++;
        }
        if (std2[i%8]==answers[i]){
            answer[1]++;
        }
        if (std3[i%10]==answers[i]){
            answer[2]++;
        }
    }
    var max=0;
    var list=[];
    for(var i =0;i<3;i++){
        if (answer[max]<answer[i]){
            
            list=[];
            list.push(i+1);
            max=i;
            console.log(list);
        }
        else if(answer[max]==answer[i]){
            list.push(i+1);
        }
    }
    console.log(answer);
    return list;
}