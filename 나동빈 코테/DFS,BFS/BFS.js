const BFS = (graph, start, visited) => {
  let queue = [start];
  visited[start] = true;

  while (queue) {
    let value = queue.shift();
    console.log(value);

    for (let i of graph[value]) {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = true;
      }
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
]

const visited = Array(graph.length).fill(false);

BFS(graph, 1, visited);