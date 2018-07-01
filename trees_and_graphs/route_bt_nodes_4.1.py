"""Route Between Nodes.

Directed graph (one-way streets)

Breadth First Search - always use a queue

"""

from enum import Enum
from myqueue import MyQueue


class State(Enum):
    Unvisited = 0
    Visiting = 1
    Visited = 2


class Node(object):

    def __init__(self, name=None):
        self.adjaceny = None # directed graph so points to 1 node/vertice
        self.state = None #State.Unvisited
        self.name = name


class Graph(object):

    def __init__(self):
        self.adjacents = [] # Nodes representing vertices


def bfs_search(graph, start, end):

    if (start == end):
        return True

    for n in graph.adjacents:
        print('setting following node to unvisited: {nme}'.format(nme=n.name))
        n.state = State.Unvisited

    q = MyQueue()
    start.state = State.Visiting
    q.add(start)

    while not q.is_empty():

        node = q.remove()

        if node is not None:
            node_adj = node.adjaceny

            if node_adj.state == State.Unvisited:

                if node_adj == end:
                    return True

                else:
                    node_adj.state = State.Visiting

                    if node_adj.adjaceny is not None:
                        q.add(node_adj)

        node.state = State.Visited

    return False


'''
0->2
1->2
2->3
3->4
'''

# create the Vertices
n0 = Node(name='zero')
n1 = Node(name='one')
n2 = Node(name='two')
n3 = Node(name='three')
n4 = Node(name='four')

# create the edges b/t
n0.adjaceny = n2
n1.adjaceny = n2
n2.adjaceny = n3
n3.adjaceny = n4
n4.adjaceny = Node() # give a dummy connection


g = Graph()
g.adjacents.append(n0)
g.adjacents.append(n1)
g.adjacents.append(n2)
g.adjacents.append(n3)
g.adjacents.append(n4)

'''
print('existing paths: ')
for i in range(len(g.adjacents)):
    print('path exists between: {s} and {e}'.format(s=g.adjacents[i].name, e=g.adjacents[i].adjaceny.name))
'''

start = n0
end = n4
print('is there a path between {start} and {end}: {val}'.format(start=start.name, end=end.name, val=bfs_search(g, start, end)))