#Functions
def bfsShortestPath(graph, startNode, endNode):
    vistedNodes = []
    queue = [startNode]
    predecessorNodes = {}

    while queue:
        currentNode = queue.pop(0)
        vistedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in vistedNodes:
                queue.append(neighbor)
                predecessorNodes[neighbor] = currentNode

    print(shortestPath(predecessorNodes, startNode, endNode))

def shortestPath(predecessorNodes, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = predecessorNodes[currentNode]
        path.append(currentNode)
    path.reverse()
    return path

#Graph
testGraph = {
    '0': ['3', '5', '9'],
    '1': ['6', '7', '4'],
    '2': ['10', '5'],
    '3': ['0'],
    '4': ['1', '5', '8'],
    '5': ['2', '0', '4'],
    '6': ['1'],
    '7': ['1'],
    '8': ['4'],
    '9': ['0'],
    '10': ['2'],
}

#Function Call
bfsShortestPath(testGraph, '0', '1')