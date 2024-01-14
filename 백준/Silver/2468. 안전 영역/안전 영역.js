const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let array = fs.readFileSync(filePath).toString().trim().split("\n");

let N = parseInt(array.shift());
for (let i = 0; i < N; i++) {
  array[i] = array[i].split(" ").map(Number);
}
let visited = new Set();

const bfs = (graph, startNode) => {
  let needVisit = [startNode]; //큐역할
  while (needVisit.length) {
    let node = needVisit.shift(); //맨 앞에서 빼기
    if (!visited.has(node)) {
      // 해당 노드 방문이 처음이라면
      visited.add(node);
      if (graph[node]) needVisit = [...needVisit, ...graph[node]]; //맨 뒤에 넣기
    }
  }
};
let vertex;
const make_graph = (copiedArray, height) => {
  //정점 만들기
  let graph = {};
  vertex = 1;

  for (let i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      if (copiedArray[i][j] >= height) {
        copiedArray[i][j] = vertex++;
      } else {
        copiedArray[i][j] = 0;
      }
    }
  }

  //간선 만들기
  let edges = [];
  for (let i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      let current = copiedArray[i][j];
      let left = copiedArray[i][j - 1];
      let up = copiedArray[i - 1] ? copiedArray[i - 1][j] : 0;

      if (current) {
        if (left) {
          edges.push([left, current]);
        }
        if (up) {
          edges.push([up, current]);
        }
      }
    }
  }
  //그래프 생성
  edges.forEach((edge) => {
    let [v, u] = edge;
    if (!graph[v]) {
      graph[v] = [];
    }
    graph[v].push(u);
    if (!graph[u]) {
      graph[u] = [];
    }
    graph[u].push(v);
  });
  return graph;
};
const cal_safe = (height) => {
  const newArray = array.map((row) => [...row]);
  graph = make_graph(newArray, height);
  let count = 0;

  for (let i = 1; i < vertex; i++) {
    if (!visited.has(i)) {
      bfs(graph, i);
      count++;
    }
  }
  visited = new Set();
  return count;
};
let max = 0;

for (let i = 0; i <= 100; i++) {
  max = Math.max(cal_safe(i), max);
}
console.log(max);
