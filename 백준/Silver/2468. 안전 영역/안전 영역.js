const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let graph = fs.readFileSync(filePath).toString().trim().split("\n");

let N = parseInt(graph.shift());
for (let i = 0; i < N; i++) {
  graph[i] = graph[i].split(" ").map(Number);
}

let dx = [-1, 1, 0, 0];
let dy = [0, 0, -1, 1];
const bfs = (visited, x, y, height) => {
  let needVisit = [[x, y]]; //큐역할
  visited[x][y] = 1;
  while (needVisit.length) {
    let [x, y] = needVisit.shift(); //맨 앞에서 빼기
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (
        nx >= 0 &&
        nx < N &&
        ny >= 0 &&
        ny < N &&
        !visited[nx][ny] &&
        graph[nx][ny] > height
      ) {
        // 해당 노드 방문이 처음이라면 , 범위 안이라면
        visited[nx][ny] = 1;
        needVisit = [...needVisit, [nx, ny]]; //맨 뒤에 넣기
      }
    }
  }
};

const cal_safe = (height) => {
  let count = 0;
  let visited = Array.from({ length: N }, () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j] && graph[i][j] > height) {
        bfs(visited, i, j, height);
        count++;
      }
    }
  }
  return count;
};
let max = 0;

for (let i = 0; i <= 100; i++) {
  //  비 높이
  max = Math.max(cal_safe(i), max);
}
console.log(max);
