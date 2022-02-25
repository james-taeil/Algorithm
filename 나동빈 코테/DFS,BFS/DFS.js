const DFS = (graph, value, visited) => {
  visited[value] = true;
  console.log(value);

  for (let i of graph[value]) {
    if (!visited[i]) {
      DFS(graph, i, visited);
    }
  }
}

const graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
];

const visited = Array(graph.length + 1).fill(false);

DFS(graph, 1, visited);