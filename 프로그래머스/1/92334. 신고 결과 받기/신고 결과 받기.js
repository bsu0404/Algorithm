function solution(id_list, report, k) {
    var answer = new Array(id_list.length).fill(0);
    var reports=[];
    var i = 0;
    var List = id_list.map(function(element){      
         return {index: i++, id: element, report: [] , reported: 0, };
    });

    
    for (var i=0;i<report.length;i++){
        reports[i] = report[i].split(" ");
        var tmp = List.find((element)=>element.id==reports[i][1]); //신고당한 사람
        // console.log(tmp.id + " " + reports[i][1]);
        
        var tmp2 = List.find((element)=>element.id==reports[i][0]); //나를 찾아서
        if(tmp2.report.indexOf(tmp.index)==-1){
            tmp2.report.push(tmp.index);
        tmp.reported++;
            
        }
    }
    
    for (var i=0;i<List.length;i++){
        for (var j = 0 ;j<List[i].report.length;j++){
            if(List[List[i].report[j]].reported>=k){
                answer[i]++;
            }
        }
    }
    
    console.log(List);
    return answer;
}