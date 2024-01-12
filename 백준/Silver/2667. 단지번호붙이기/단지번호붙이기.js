const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
//그래프 만들기 - 정점
let array = input.slice(1);
for (let i = 0; i < array.length; i++) {
  array[i] = Array.from(array[i], Number);
}
let vertex = 1;
for (let i = 0; i < array.length; i++) {
  for (let j = 0; j < array.length; j++) {
    if (array[i][j] == 1) {
      array[i][j] = vertex++;
    }
  }
}

//그래프 만들기 - 간선
edges = [];
for (let i = 0; i < array.length; i++) {
  for (let j = 0; j < array.length; j++) {
    let current = array[i][j];
    let left = array[i][j - 1] ? array[i][j - 1] : 0; //왼쪽
    let up = array[i - 1] ? array[i - 1][j] : 0; //위
    if (current != 0) {
      if (left != 0) {
        edges.push([left, current]);
      }
      if (up != 0) {
        edges.push([up, current]);
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
for (const key in graph) {
  graph[key] = graph[key].sort((a, b) => a - b);
}

//bfs
const bfs = (startNode) => {
  let needVisit = [startNode]; //큐역할
  let count = 0;
  while (needVisit.length) {
    let node = needVisit.shift(); //맨 앞에서 빼기
    if (!visited.has(node)) {
      // 해당 노드 방문이 처음이라면
      count++;
      visited.add(node);
      if (graph[node]) needVisit = [...needVisit, ...graph[node]]; //맨 뒤에 넣기
    }
  }
  return count;
};
let visited = new Set();
let results = [];
let count = 0;
for (let i = 1; i < vertex; i++) {
  if (!visited.has(i)) {
    count++;
    results.push(bfs(i));
  }
}
results.sort((a, b) => a - b);
results.unshift(count);
console.log(results.join("\n"));
