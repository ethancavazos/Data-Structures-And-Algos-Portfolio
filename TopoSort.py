#  File: TopoSort.py

#  Description: Assignment 24

#  Course Name: CS 313E

#  Date Created: 11/27/2020

#  Date Last Modified: 12/2/2020

import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, thing):
        self.stack.append(thing)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, thing):
        self.queue.append(thing)

    def dequeue(self,thing):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        stop = self.get_index(toVertexLabel)

        # no edge is if both don't exist
        if start == -1 or stop == -1:
            return -1

        wt = self.adjMat[start][stop]
        # ELSE
        # get wt from adj mat
        if wt > 0:
            return self.adjMat[start][stop]
        elif wt == 0 or wt < 0:
            return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        nVert = len(self.Vertices)

        start = self.get_index (vertexLabel)
        neighbors = []


        if start == -1:
            return neighbors

        for i in range (nVert):

            if self.adjMat [start][i] > 0:
                neighbors.append(i)

        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    def get_adj_vert(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):

        vertices = []
        nVert = len(self.Vertices)

        for i in range (nVert):
            verts = (self.Vertices[i]).label
            vertices.append(verts)

        return vertices

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create da queue
        theQ = Queue()

        # mark vertex visited
        self.Vertices[v].visited = True
        print(self.Vertices[v])

        theQ.enqueue(v)
        current = v
        x = self.get_adj_unvisited_vertex(current)

        # visit other vertices in b
        while not theQ.is_empty():

            # get next unvisited vertex
            if x == -1:

                x = theQ.dequeue()
                current = x
                x = self.get_adj_unvisited_vertex(current)

            else:

                # next
                if self.Vertices[x].visited == False:
                    print(self.Vertices[x])
                    self.Vertices[x].visited = True

                theQ.enqueue(x)
                x = self.get_adj_unvisited_vertex(current)

        # the queue is empty
        # make all visited false again
        nVert = len(self.Vertices)

        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        start = self.get_index (fromVertexLabel)
        stop = self.get_index (toVertexLabel)

        if start == -1 or stop == -1:
            return

        self.adjMat[start][stop] = 0
        self.adjMat[stop][start] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        idx = self.get_index (vertexLabel)
        if idx == -1:
            return


        # delete edgez in adj mat
        nVert = len(self.Vertices)
        for i in range (nVert):
            # deleting the column
            self.adjMat[i].pop(idx)


        temp = []
        for i in range (nVert):
            # deleting row

            if i != idx:
                temp.append(self.adjMat[i])


        self.adjMat = temp

        # DELETE VERTEX
        self.Vertices.pop(idx)

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self):

        # create the Stack
        theStack = Stack()

        nVert = len(self.Vertices)
        visited = [False] * nVert

        for i in range(nVert):

            if self.Vertices[i].visited == False:
                if self.has_cycler(i, visited):

                    nVert = len(self.Vertices)

                    for i in range(nVert):
                        (self.Vertices[i]).visited = False
                    return True

        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return False


    def has_cycler(self, i, visited):

        visited[i] = True
        self.Vertices[i].visited = True
        neighbors = self.get_neighbors(self.Vertices[i].get_label())


        # Neighbors
        for node in neighbors:

            # If visited
            if visited[self.get_index(node)] is True:
                return True

            elif self.has_cycler(self.get_index(node), visited):
                return True

        # no cycle
        return False


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):

        nVert = len(self.Vertices)

        # Determine all in degrees

        degrees = [0] * nVert
        for i in range(nVert):
            degrees[i] = self.topoSorter(i)

        topo = []
        sub = []

        while len(topo) != nVert:

            # sprt topo

            for i in range(nVert):
                if not self.Vertices[i].was_visited():

                    if degrees[i] == 0:
                        # Add current node to sublist w/ that degree

                        sub.append(self.Vertices[i].get_label())
                        self.Vertices[i].visited = True

                        # all neighbors-one incident edge
                        neighbors = self.get_neighbors(self.Vertices[i])
                        for node in neighbors:
                            if degrees[i] != 0:
                                degrees[i] -= 1

            # Decrease all in-degree by 1 if none of deg 0
            if len(sub) == 0:
                for i in range(nVert):
                    degrees[i] -= 1

            # Sort Sublist alphabetly

            else:
                sub.sort()
                # Enqueue the items in the sublist
                for i in range(len(sub)):
                    topo.append(sub[i])

            # Reset sublist
            sub = []

        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return topo


    def topoSorter(self, i):

        nVert = len(self.Vertices)
        countr = 0

        for t in range(nVert):

            if self.adjMat[t][i] != 0:
                countr += 1

        return countr


def main():
    # create a Graph object
    theGraph = Graph()

    # input
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    for i in range(num_vertices):
        node = sys.stdin.readline()
        node = node.strip()

        theGraph.add_vertex(node)

    # edges
    num_edges = int ((sys.stdin.readline()).strip())

    for i in range(num_edges):
        edge = (sys.stdin.readline()).strip()
        edge = edge.split()
        start = edge[0]
        finish = edge[1]

        theGraph.add_directed_edge(theGraph.get_index(start) , theGraph.get_index(finish) )


    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print ("The Graph has a cycle.")
    else:
        print ("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print ("\nList of vertices after toposort")
        print (vertex_list)

main()
