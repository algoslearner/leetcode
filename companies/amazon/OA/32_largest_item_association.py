'''
Question:
In order to improve customer experience, Amazon has developed a system to provide recommendations to the customer regarding the item they can purchase. Based on historical customer purchase information, an item association can be defined as - If an item A is ordered by a customer, then item B is also likely to be ordered by the same customer (e.g. Book 1 is frequently orderered with Book 2). All items that are linked together by an item association can be considered to be in the same group. An item without any association to any other item can be considered to be in its own item association group of size 1.

Given a list of item association relationships(i.e. group of items likely to be ordered together), write an algorithm that outputs the largest item association group. If two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.

Input
The itput to the function/method consists of an argument - itemAssociation, a list containing paris of string representing the items that are ordered together.

Output
Return a list of strings representing the largest association group sorted lexicographically.

Example
Input:
itemAssociation: [
[Item1, Item2],
[Item3, Item4],
[Item4, Item5]
]

Output:
[Item3, Item4, Item5]

Explanation:
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3,Item4,Item5]
In the available associations, group2 has the largest association. So, the output is [Item3, Item4, Item5].
'''

##################################################################################################
# Python solution using DFS

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacentNodes = {}

# V: num of items
# E: num of associations
# Time: O(V + E)
# Space: O(V + E)

def largestItemAssociation(itemAssociation):
    graph = {}
    for dependent, dependency in itemAssociation:
        if dependent not in graph:
            graph[dependent] = Node(dependent)
        if dependency not in graph:
            graph[dependency] = Node(dependency)
        graph[dependent].adjacentNodes[dependency] = graph[dependency]

    visited = set()
    largestLength, output = 0, []
    for item, node in graph.items():
        if item in visited:
            continue

        def DFS(cur, res):
            nonlocal largestLength
            visited.add(cur.name)
            if len(cur.adjacentNodes) == 0:
                if (len(res) + 1) < largestLength:
                    return
                elif (len(res) + 1) > largestLength:
                    output.clear()

                largestLength = len(res) + 1
                output.append(res + [cur.name])
                return
            for neighbor, nNode in cur.adjacentNodes.items():
                DFS(nNode, res + [cur.name])
        DFS(node, [])

    if len(output) > 1:
        output.sort()
    return output[0]


if __name__ == '__main__':
    print(largestItemAssociation([
    ['Item1', 'Item2'],
    ['Item3', 'Item4'],
    ['Item4', 'Item5'],
    ['Item4', 'Item6']
]))
    
#######################################################################################################
# class Item():
    def __init__(self, name):
        self.name = name
        self.edges = set()

    def add_edge(self, other_item):
        self.edges.add(other_item)

    def __repr__(self):
        return self.name

def findLargestAssociationGroup(assns):
    # build undirected graph
    all_nodes = {}
    for assn in assns:
        left = all_nodes.get(assn[0], Item(assn[0]))
        right = all_nodes.get(assn[1], Item(assn[1]))
        left.add_edge(right)
        right.add_edge(left)
        all_nodes[assn[0]] = left
        all_nodes[assn[1]] = right

    # do DFS and keep removing from map
    # each DFS would traverse a connected component
    # of the graph
    q = deque()

    all_connected_comps = []
    while all_nodes:
        q.append(all_nodes[list(all_nodes.keys())[0]])
        connected_comps = []
        visited = set()
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                connected_comps.append(node.name)
                if node.name in all_nodes:
                    del all_nodes[node.name]

                for vertex in node.edges:
                    q.appendleft(vertex)
        all_connected_comps.append((len(connected_comps), connected_comps))

    return sorted(all_connected_comps, key=lambda x: x[0], reverse=True)[0][1]
