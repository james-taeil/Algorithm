function solution(n, edge) {
    return bfs(edge, 1, n);
}

const bfs = (edges, start, end) => {
    let visit = new Array(end + 1);
    let lev = new Array(end + 1).fill(0);
    let queue = [start];
    let now;
    visit[start] = true;
    
    while (queue.length) {
        let node = queue.shift();
        now = lev[node] + 1;
        for (let edge of edges) {
            if (edge[0] === node && visit[edge[1]] === undefined) {
                queue.push(edge[1]);
                visit[edge[1]] = true;
                lev[edge[1]] = now;
            } else if (edge[1] === node && visit[edge[0]] === undefined) {
                queue.push(edge[0]);
                visit[edge[0]] = true;
                lev[edge[0]] = now;
            }
        }
    }
    return lev.filter((el) => el === now - 1).length;
}