function solution(sizes) {
    var answer = 0;
    maxX=-Infinity;
    maxY=-Infinity;
    for (var i =0;i<sizes.length;i++){
        maxX=Math.max(Math.min(sizes[i][0],sizes[i][1]),maxX);
        maxY=Math.max(Math.max(sizes[i][0],sizes[i][1]),maxY);
    }
    return maxX*maxY;
}