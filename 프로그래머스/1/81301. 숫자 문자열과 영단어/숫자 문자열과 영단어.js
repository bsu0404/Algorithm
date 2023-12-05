function solution(s) {
    var str = s;
    var number =["zero","one","two","three","four","five","six","seven","eight","nine"];
    for (var i =0;i<10;i++){
       str = str.replace(new RegExp(number[i], 'g'), i);  
    }
  
   
    return parseInt(str);
}