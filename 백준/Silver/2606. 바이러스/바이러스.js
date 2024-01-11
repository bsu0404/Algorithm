const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
//input 정리 및 초기화
const N = parseInt(input[0]);
const M = parseInt(input[1]);

const edges = input.slice(2);
for (let i = 0; i < M; i++) {
  edges[i] = edges[i].split(" ").map(Number);
}
let count = 0;

//그래프 구현
let graph = {};
edges.forEach((edge) => {
  let [vertex1, vertex2] = edge;
  if (!graph[vertex1]) {
    graph[vertex1] = [];
  }
  graph[vertex1].push(vertex2);

  if (!graph[vertex2]) {
    graph[vertex2] = [];
  }
  graph[vertex2].push(vertex1);
});
for (const key in graph) {
  graph[key] = graph[key].sort((a, b) => a - b);
}
//bfs
const bfs = (startNode) => {
  let visited = new Set();
  let needVisit = [startNode]; //큐역할
  let results = [];
  while (needVisit.length) {
    let node = needVisit.shift(); //맨 앞에서 빼기
    if (!visited.has(node)) {
      // 해당 노드 방문이 처음이라면
      count++;
      visited.add(node);
      if (graph[node]) needVisit = [...needVisit, ...graph[node]]; //맨 뒤에 넣기
    }
  }
};
bfs(1);
console.log(count - 1);
