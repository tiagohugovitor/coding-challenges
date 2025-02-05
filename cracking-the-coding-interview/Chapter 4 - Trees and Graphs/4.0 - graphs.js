export class GraphAdjacencyList {
    constructor() {
        this.adjList = new Map();
    }

    addVertex(vertex) {
        if (!this.adjList.has(vertex)) {
            this.adjList.set(vertex, []);
        }
    }

    addEdge(vertex1, vertex2, isDirected = true) {
        if (!this.adjList.has(vertex1)) this.addVertex(vertex1);
        if (!this.adjList.has(vertex2)) this.addVertex(vertex2);

        this.adjList.get(vertex1).push(vertex2);

        if (!isDirected) {
            this.adjList.get(vertex2).push(vertex1);
        }
    }

    removeEdge(vertex1, vertex2) {
        if (this.adjList.has(vertex1)) {
            this.adjList.set(vertex1, this.adjList.get(vertex1).filter(v => v !== vertex2));
        }
        if (this.adjList.has(vertex2)) {
            this.adjList.set(vertex2, this.adjList.get(vertex2).filter(v => v !== vertex1));
        }
    }

    removeVertex(vertex) {
        this.adjList.delete(vertex);
        for (let [key, neighbors] of this.adjList) {
            this.adjList.set(key, neighbors.filter(v => v !== vertex));
        }
    }

    display() {
        for (let [vertex, neighbors] of this.adjList) {
            console.log(`${vertex} -> ${neighbors.join(", ")}`);
        }
    }
}

export class GraphAdjacencyMatrix {
    constructor(size) {
        this.size = size;
        this.matrix = Array.from({ length: size }, () => Array(size).fill(0));
    }

    addEdge(vertex1, vertex2, isDirected = false) {
        this.matrix[vertex1][vertex2] = 1;
        if (!isDirected) {
            this.matrix[vertex2][vertex1] = 1;
        }
    }

    removeEdge(vertex1, vertex2) {
        this.matrix[vertex1][vertex2] = 0;
        this.matrix[vertex2][vertex1] = 0;
    }

    display() {
        console.log("   " + Array.from({ length: this.size }, (_, i) => i).join(" "));
        this.matrix.forEach((row, i) => {
            console.log(i + " | " + row.join(" "));
        });
    }
}
