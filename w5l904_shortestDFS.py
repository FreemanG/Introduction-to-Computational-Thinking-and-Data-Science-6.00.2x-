from graph import *

#def DFS(graph, start, end, path = [], shortest = None):
#    #assumes graph is a Digraph
#    #assumes start and end are nodes in graph
#    path = path + [start]
#    print 'Current dfs path:', printPath(path)
#    if start == end:
#        return path
#    for node in graph.childrenOf(start):
#        if node not in path: #avoid cycles
#            newPath = DFS(graph,node,end,path,shortest)
#            if newPath != None:
#                return newPath

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def DFS2(digraph, start, end, path = [], res = [], recur = 0):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph 
    recur += 1 # depth of recursion
    path = path + [start]
    if start == end:
        res.append(path)
    
    for node in digraph.childrenOf(start):
        if node not in path: #avoid cycles
            DFS(digraph, node, end, path, res, recur)
                
    if recur == 1 and node == digraph.childrenOf(start)[-1]:
        return res 

def printPath2(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        for j in range(len(path[i])):
            if j == len(path[i]) - 1:
                result = result + str(path[i][j]) + '\n'
            else:
                result = result + str(path[i][j]) + '->'
    return result

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS2(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath2(sp)