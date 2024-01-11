const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let [N, M, V] = input[0].split(" ").map(Number); //정점 수, 간선 수, 시작
let edges = input.slice(1);
for (let i = 0; i < M; i++) {
  edges[i] = edges[i].split(" ").map(Number);
}
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
const dfs = (startNode) => {
  let visited = new Set();
  let needVisit = [startNode]; //스택

  let results = [];
  while (needVisit.length) {
    const node = needVisit.shift(); //맨 앞에서 빼기
    if (!visited.has(node)) {
      results.push(node);
      visited.add(node);
      if (graph[node]) needVisit = [...graph[node], ...needVisit]; //맨 앞에 추가
    }
  }
  console.log(results.join(" "));
};

const bfs = (startNode) => {
  let visited = new Set();
  let needVisit = [startNode]; //큐역할
  let results = [];
  while (needVisit.length) {
    let node = needVisit.shift(); //맨 앞에서 빼기
    if (!visited.has(node)) {
      // 해당 노드 방문이 처음이라면
      results.push(node);
      visited.add(node);
      if (graph[node]) needVisit = [...needVisit, ...graph[node]]; //맨 뒤에 넣기
    }
  }
  console.log(results.join(" "));
};
dfs(V);
bfs(V);
