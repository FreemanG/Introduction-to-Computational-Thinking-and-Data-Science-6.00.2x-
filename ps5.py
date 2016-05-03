# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    # creat a WeightedGraph object
    g = WeightedDigraph()
    # inFile: file
    inFile = open(mapFilename)
    # creat directed graph representing the map
    count = 0
    for line in inFile:
        fields = line.split()
        count += 1
        # Node and Edge
        scr = Node(int(fields[0]))
        dest = Node(int(fields[1]))
        edge = WeightedEdge(scr, dest, float(fields[2]), float(fields[3]))
        # add Node and Edge to the graph
        try:
            g.addNode(scr)
            g.addNode(dest)
        except:
            pass
        g.addEdge(edge)
    print "Loading map from file..."
    return g
        
        
#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def DFS(digraph, start, end, path = [], res = [], recur = 0):
    # record path
    recur += 1 # depth of recursion
    path = path + [start]
    if start == end:
        res.append(path)
    # depth first search
    for node in digraph.childrenOf(Node(start)):
        #avoid cycles
        if str(node[0]) not in path: 
            DFS(digraph, str(node[0]), end, path, res, recur)          
    # return res
    try:
        if recur == 1 and node == digraph.childrenOf(Node(start))[-1]:
            return res
    except:
        pass

def DIS(digraph, res, constrain):
    # sum distance
    dis = []
    for path in range(len(res)): #path
        dis.append(0)
        for i in range(len(res[path]) - 1): #start node
            for j in digraph.edges[Node(int(res[path][i]))]: #edge
                if j[0].getName() == res[path][i+1]:
                    dis[path] += int(j[1][constrain]) #weight
    return dis
                    
                    
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    Path = []
    res_Path = []
    res_Dist = []
    shortest_Path = None
    
    Path = DFS(digraph, start, end, [], [])
    if not(Path == None):
        ttlDis = DIS(digraph, Path, 0)
        outDis = DIS(digraph, Path, 1)
    else:
        raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')    

    for i in range(len(Path)):
        if outDis[i] < maxDistOutdoors or outDis[i] == maxDistOutdoors: 
            res_Path.append(Path[i])
            res_Dist.append(ttlDis[i])
    if not(res_Path == []):
        shortest_Dist = res_Dist[0]
        for i in range(len(res_Path)):
            if res_Dist[i] < maxTotalDist or res_Dist[i] == maxTotalDist:
                if res_Dist[i] < shortest_Dist or res_Dist[i] == shortest_Dist:
                    shortest_Path = res_Path[i]
                    shortest_Dist = res_Dist[i]
        if not(shortest_Path == None):
            return shortest_Path
        else:
            raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')
    else:
        raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')


##############################################################################  
#map5 = WeightedDigraph()
#na = Node(1)
#nb = Node(2)
#nc = Node(3)
#nd = Node(4)
#ne = Node(5)
#
#e1 = WeightedEdge(na, nb, 5, 2)
#e2 = WeightedEdge(nc, ne, 6, 3)
#e3 = WeightedEdge(nb, nc, 20, 10)
#e4 = WeightedEdge(nb, nd, 10, 5)
#e5 = WeightedEdge(nd, nc, 2, 1)
#e6 = WeightedEdge(nd, ne, 20, 10)
#
#map5.addNode(na)
#map5.addNode(nb)
#map5.addNode(nc)
#map5.addNode(nd)
#map5.addNode(ne)
#
#map5.addEdge(e1)
#map5.addEdge(e2)
#map5.addEdge(e3)
#map5.addEdge(e4)
#map5.addEdge(e5)
#map5.addEdge(e6)

#bruteForceSearch(map5, "1", "3", 17, 8)
#bruteForceSearch(map5, "1", "5", 23, 11)
#bruteForceSearch(map5, "4", "5", 21, 11)
#bruteForceSearch(map5, "5", "1", 100, 100)
#bruteForceSearch(map5, "4", "5", 8, 2)

#directedDFS(map5, "1", "3", 17, 8)
#directedDFS(map5, "1", "5", 23, 11)
#directedDFS(map5, "4", "5", 21, 11)
#directedDFS(map5, "5", "1", 100, 100)
#directedDFS(map5, "4", "5", 8, 2)
############################################################################## 
##############################################################################  
#map6 = WeightedDigraph()
#na = Node(1)
#nb = Node(2)
#nc = Node(3)
#nd = Node(4)
#ne = Node(5)
#
#e1 = WeightedEdge(na, nb, 5, 2)
#e2 = WeightedEdge(nc, ne, 5, 1)
#e3 = WeightedEdge(nb, nc, 20, 10)
#e4 = WeightedEdge(nb, nd, 10, 5)
#e5 = WeightedEdge(nd, nc, 5, 1)
#e6 = WeightedEdge(nd, ne, 20, 1)
#
#map6.addNode(na)
#map6.addNode(nb)
#map6.addNode(nc)
#map6.addNode(nd)
#map6.addNode(ne)
#
#map6.addEdge(e1)
#map6.addEdge(e2)
#map6.addEdge(e3)
#map6.addEdge(e4)
#map6.addEdge(e5)
#map6.addEdge(e6)

#bruteForceSearch(map6, "1", "5", 35, 9)
#bruteForceSearch(map6, "1", "5", 35, 8)
#bruteForceSearch(map6, "4", "5", 21, 11)
#bruteForceSearch(map6, "4", "5", 21, 1)
#bruteForceSearch(map6, "4", "5", 19, 1)
#bruteForceSearch(map6, "3", "2", 100, 100)
#bruteForceSearch(map6, "4", "5", 8, 2)

#directedDFS(map6, "1", "5", 35, 9)
#directedDFS(map6, "1", "5", 35, 8)
#directedDFS(map6, "4", "5", 21, 11)
#directedDFS(map6, "4", "5", 21, 1)
#directedDFS(map6, "4", "5", 19, 1)
#directedDFS(map6, "3", "2", 100, 100)
#directedDFS(map6, "4", "5", 8, 2)
##############################################################################   
    
#
# Problem 4: Finding the Shorest Path using Optimized Search Method
# 
#{source_node:[ [dest_node, (total_dist, outdoor_dist) ], [dest_node, (total_dist, outdoor_dist) ] ] }
#{a: [[b,(2,1)], [c,(3,2)]], b: [[c,(4,2)]], c:[] }   
    
def DFS2(digraph, start, end, constrain, path = [], res = [], recur = 0):
    # record path
    recur += 1 # depth of recursion
    path = path + [start]
    if start == end:
        res.append(path)
    # shortest node
    if not(digraph.childrenOf(Node(start)) == []):
        shortest_Node = None
        shortest_Dist = int(digraph.childrenOf(Node(start))[0][1][constrain])
        for i in digraph.childrenOf(Node(start)):
            if int(i[1][constrain]) < shortest_Dist or int(i[1][constrain]) == shortest_Dist:
                shortest_Dist = int(i[1][constrain])
                shortest_Node = str(i[0])
        # avoid cycles   
        if str(shortest_Node) not in path: 
            DFS2(digraph, str(shortest_Node), end, constrain, path, res, recur)          
    # return res
    try:
        if recur == 1:
            return res
    except:
        pass    

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    Path = []
    res_Path = []
    res_Dist = []
    shortest_Path = None
    
    Path_ttl = DFS2(digraph, start, end, 0, [], [])
    Path_out = DFS2(digraph, start, end, 1, [], [])
    Path = Path_ttl + Path_out # all Path
    if not(Path == None):
        ttlDis = DIS(digraph, Path, 0)
        outDis = DIS(digraph, Path, 1)
    else:
        raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')
    
    for i in range(len(Path)):
        if outDis[i] < maxDistOutdoors or outDis[i] == maxDistOutdoors: 
            res_Path.append(Path[i])
            res_Dist.append(ttlDis[i])
    if not(res_Path == []):
        shortest_Dist = res_Dist[0]
        for i in range(len(res_Path)):
            if res_Dist[i] < maxTotalDist or res_Dist[i] == maxTotalDist:
                if res_Dist[i] < shortest_Dist or res_Dist[i] == shortest_Dist:
                    shortest_Path = res_Path[i]
                    shortest_Dist = res_Dist[i]
        if not(shortest_Path == None):
            return shortest_Path
        else:
            raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')
    else:
        raise ValueError('there exists no path that satisfies maxTotalDist and maxDistOutdoors constraints')

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges
#
#
#     LARGE_DIST = 1000000
#
#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)
#
#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)
#
#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
#
#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
#
#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
#
#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
#
#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
#    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
#
#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
#    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
#    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
