
/*
https://leetcode.com/problems/all-paths-from-source-to-target/
*/
var allPathsSourceTarget = function(graph) {
    let seed = [[0]]           // starting point
    let N = graph.length - 1   // idx of last node
    let R = []                 // result
    const last = (a) => a[a.length-1];
    
    // from every node travel to all unvisited neighbour nodes
    // track each path visited
    while (seed.length > 0) {
        let S = []
        for (const s of seed) {
            for (const g of graph[last(s)]) {
                // if end reached add path to result array
                // otherwise add visiting node to path
                ((g == N) ? R : S).push([...s, g])
            }
        }
        seed = S;
    }
    return R;
};
