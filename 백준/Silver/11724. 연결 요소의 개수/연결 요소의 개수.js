const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let edges = fs.readFileSync(filePath).toString().trim().split("\n");

let [N, M] = edges.shift().split(" ").map(Number); // 정점수, 간선수

// 간선
for (let i = 0; i < M; i++) {
  edges[i] = edges[i].split(" ").map(Number);
}
// 그래프 구현
let graph = {};
edges.forEach((edge) => {
  let [u, v] = edge;
  if (!graph[u]) {
    graph[u] = [];
  }
  graph[u].push(v);
  if (!graph[v]) {
    graph[v] = [];
  }
  graph[v].push(u);
});

let visited = new Set();
const dfs = (node) => {
  if (!visited.has(node)) {
    visited.add(node);
    if (graph[node]) {
      graph[node].forEach((neighbor) => {
        dfs(neighbor);
      });
    }
  }
};

let count = 0;
for (let i = 1; i < N + 1; i++) {
  if (!visited.has(i)) {
    dfs(i);
    count++;
  }
}
console.log(count);
