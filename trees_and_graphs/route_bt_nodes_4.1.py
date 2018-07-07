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
        self.state = State.Unvisited
        self.name = name


class Graph(object):
    def __init__(self):
        self.adjacents = [] # Nodes representing vertices


def dfs_search(graph, start, end):

    print('evaluating following node: {n}'.format(n=start.name))
    print('does {s} == {e}... '.format(s=start.name, e=end.name))

    if start == end:
        print('start and end nodes the same:  {s} == {e}... '.format(s=start.name, e=end.name))
        return True
    else:
        start.state = State.Visited

    node_adj = start.adjaceny

    if node_adj is not None and node_adj.state == State.Unvisited:
        return dfs_search(graph, node_adj, end)
    else:
        return False


def bfs_search(graph, start, end):

    if (start == end):
        return True

    for n in graph.adjacents:
        # print('setting following node to unvisited: {nme}'.format(nme=n.name))
        n.state = State.Unvisited

    q = MyQueue()
    start.state = State.Visiting
    q.add(start)

    while not q.is_empty():

        node = q.remove()

        if node is not None:
            node_adj = node.adjaceny


            if node_adj.state == State.Unvisited:

                print('evaluating following node: {n}'.format(n=node_adj.name))

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


start = n0
end = n3
print('BFS: is there a path between {start} and {end}: {val}\n'.format(start=start.name, end=end.name, val=bfs_search(g, start, end)))


for node in g.adjacents:
    print('resetting state of nodes between tests: node={nme} before_state={bst} after_state={ast}'.format(nme=node.name, bst=node.state, ast=State.Unvisited))
    node.state = State.Unvisited


start = n0
end = n3
print('DFS: is there a path between {start} and {end}: {val}\n'.format(start=start.name, end=end.name, val=dfs_search(g, start, end)))
