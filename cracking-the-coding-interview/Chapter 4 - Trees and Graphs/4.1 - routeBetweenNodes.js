import { MyQueue } from "../Chapter 3 - Stacks and Queues/3.0 - stackAndQueuesUtils.js"
import { GraphAdjacencyList } from "./4.0 - graphs.js"

const DFS = (graph, node, visit, visited) => {
    if (visited.has(node)) return false

    visited.add(node)
    if (visit(node)) return true

    for (const child of graph.adjList.get(node)) {
        if (DFS(graph, child, visit, visited)) return true
    }

    return false
}

const BFS = (graph, root, visit) => {
    const queue = new MyQueue
    queue.enqueue(root)
    const visited = new Set()

    while (!queue.isEmptyQueue()) {
        const current = queue.dequeue() 
        
        if (visited.has(current)) continue
        
        visited.add(current)
        
        if (visit(current)) return true
        
        for (const child of graph.adjList.get(current)) {
            queue.enqueue(child)
        }
    }
    
    return false
}

const routeBetweenNodesDFS = (graph, start, target) => {
    const visit = (node) => node === target
    return DFS(graph, start, visit, new Set())
}

const routeBetweenNodesBFS = (graph, start, target) => {
    const visit = (node) => node === target
    return BFS(graph, start, visit)
}

const graph = new GraphAdjacencyList();
graph.addEdge(0, 1);
graph.addEdge(0, 2);
graph.addEdge(1, 3);
graph.addEdge(2, 3);
graph.addEdge(3, 4);
graph.addEdge(4, 5);
graph.display();

console.log("DFS busca do 0 ao 5:", routeBetweenNodesDFS(graph, 0, 5)); // true
console.log("BFS busca do 0 ao 5:", routeBetweenNodesBFS(graph, 0, 5)); // true
console.log("DFS busca do 0 ao 6:", routeBetweenNodesDFS(graph, 0, 6)); // false
console.log("BFS busca do 0 ao 6:", routeBetweenNodesBFS(graph, 0, 6)); // false