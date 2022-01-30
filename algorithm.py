#Functions
def bfsShortestPath(graph, startNode, endNode): #Takes in 3 parameters the graph, startNode, and endNode
    vistedNodes = [] #Stores all visted nodes to make sure doesn't loop over nodes
    queue = [startNode] #Initilies the queue with the starting node
    predecessorNodes = {} #Dictionary that stores the parent of every node visited, Fills when visting a new neighbour. Is used to back track the shortest path from the start node to the end node

    while queue: #While the queue in not empty
        currentNode = queue.pop(0) #Pops the first element from the queue and stores it in currentNode
        vistedNodes.append(currentNode) #Mark the currentNode as visted
        for neighbour in graph[currentNode]: #Itterate through all neighbours
            if neighbour not in vistedNodes: #Check if the neighbour is already visited
                queue.append(neighbour) #Append it to the queue
                predecessorNodes[neighbour] = currentNode #Sets the parent of the current neighbour to the current node

    print(shortestPath(predecessorNodes, startNode, endNode)) #Function call

def shortestPath(predecessorNodes, startNode, endNode):
    path = [endNode] #Initialized with only the endNode
    currentNode = endNode #Sets the currentNode to the endNode
    while currentNode != startNode: #Goes backwards through all parent nodes till it reaches the startNode
        currentNode = predecessorNodes[currentNode] #Sets the currentNode to the predecessorNode
        path.append(currentNode) #Adds the currentNode to the path, adds to the path backwards (endNode -> startNode)
    path.reverse() #Reverse the order of the path
    return path #Returns path

#Graph
testGraph = { #Dictionary to stores all the nodes and there connections
    'A': ['B', 'D', 'G', 'H'],
    'B': ['D', 'H'],
    'C': ['D', 'E', 'G'],
    'D': ['F', 'G', 'H'],
    'E': ['F'],
    'F': ['G', 'H'],
    'G': ['H', 'E'],
    'H': ['E', 'C'],
}

#Function Call
bfsShortestPath(testGraph, 'A', 'C')