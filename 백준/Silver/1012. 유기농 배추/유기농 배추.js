const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let T = parseInt(input.shift());

let visited = new Set();

const make_graph = (N, M, K) => {
  let vertices = [];
  for (let i = 0; i < K; i++) {
    vertices.push(input.shift());
    vertices[i] = vertices[i].split(" ").map(Number);
  }
  //정점 찍기
  let array = Array.from({ length: N }, () => Array(M).fill(0));
  let vertex = 1;
  for (let i = 0; i < K; i++) {
    let [a, b] = vertices[i];
    array[a][b] = vertex++;
  }
  //간선 만들기
  let edges = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      const current = array[i][j];
      if (current != 0) {
        const up = array[i - 1] ? array[i - 1][j] : 0;
        const left = array[i] ? array[i][j - 1] : 0;
        if (up) {
          edges.push([up, current]);
        }
        if (left) {
          edges.push([left, current]);
        }
      }
    }
  }
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
  return graph;
};
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
const cal_count = () => {
  let [N, M, K] = input.shift().split(" ").map(Number); //가로, 세로, edge수

  let graph = make_graph(N, M, K);
  let count = 0;

  for (let i = 1; i <= K; i++) {
    if (!visited.has(i)) {
      bfs(graph, i);
      count++;
    }
  }
  visited = new Set();
  return count;
};

for (let i = 0; i < T; i++) {
  console.log(cal_count());
}
