import functools
from collections import deque

def topologicalSort(graph):
    """
    returns a topological ordering L of the vertices
    """
    L = deque()
    marked = set()
    tmp_mark = set()

    def visit(vertex):
        if vertex in marked:
            return
        if vertex in tmp_mark:
            print("ERROR: THE GRAPH IS NOT ACYCLIC") # should not happen TM
            return
        tmp_mark.add(vertex)

        if vertex in graph:
            for w in graph[vertex]:
                visit(w)
        
        marked.add(vertex)
        L.appendleft(vertex)
    

    for v in graph:
        if v not in marked:
            visit(v)
    
    return L


data = open('input05').read().split('\n')

dependency_graph = {}

correct = 0

# build graph
for line in data:
    if '|' in line:
        rule = [int(x) for x in line.split('|')]

        if rule[0] in dependency_graph:
            dependency_graph[rule[0]].append(rule[1])
        else:
            dependency_graph[rule[0]] = [rule[1]]
        if not rule[1] in dependency_graph:
            dependency_graph[rule[1]] = []

topological_order = topologicalSort(dependency_graph)
position = {v : i for i, v in enumerate(topological_order)}

# check lines
correct = 0
sum = 0
for line in data:
    if '|' in line or line == "":
        continue
    
    sequence = [int(x) for x in line.split(',')]
    chopped_sequence = [x for x in sequence if x in dependency_graph]
    mapped_sequence = [position[v] for v in chopped_sequence]
    if sorted(mapped_sequence) == mapped_sequence:
        correct += 1
        sum += sequence[len(sequence) // 2]
        # print("Original={}, chopped={}, mapped={}".format(sequence, chopped_sequence, mapped_sequence))

print("The number of correctly issued updates is {} and the middle pages sum to {}".format(correct, sum))