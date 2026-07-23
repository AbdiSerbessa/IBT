## exercise 1
class Node:
    def __init__(self,value):
        self.value = value
        self.left =  None
        self.right = None

def insert (root,value):
    if root is None:
        return Node(value)
    if value<root.value:
        root.left = insert(root.left,value)
    elif value>root.value:
        root.right = insert(root.right,value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print (root.value,end=" ")
        inorder_traversal(root.right)

values_to_insert = [45,15,79,90,10,55,12,20,50]

root =None
for val in values_to_insert:
    root = insert(root, val)

print("In-order Traversal (sorted output)")
inorder_traversal(root)
print()    



##exercise 2

class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None
def height(node):
    if node is None:
        return 0
    left_depth = height(node.left)
    right_depth =height(node.right)
    return 1 + max(left_depth,right_depth)

root = Node(45)
root.left = Node(15)
root.right = Node(79)
root.left.left =Node(10)

print("Tree height / Max depth: ",height(root))




##exercise 3
from collections import deque

def bfs(graph,start):
    visited = set([start])
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

graph = {

     'A':['B','C'],
     'B': ['A','D','E'],
     'C':['A','F'],
     'D':['B'],
     'E':['B','F'],
     'F':['C','E'],
     'G':['H'],
     'H':['G']

    }
start_node = 'A'
reachable = bfs(graph,start_node)

print(f"reachable vertices starting from '{start_node}':",reachable)




####Exercise 4

from collections import deque

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def bfs_order(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited    


graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

start_node = 'A'
    
dfs_result = dfs_recursive(graph, start_node)
bfs_result = bfs_order(graph, start_node)

print("DFS Order (Depth-First):", " -> ".join(dfs_result))
print("BFS Order (Breadth-First):", " -> ".join(bfs_result))








###Exercise 5

import heapq
tasks = [
    (3, "Write documentation"),
    (1, "Fix critical production bug"),
    (5, "Clean up temp files"),
    (2, "Review pull request"),
    (4, "Refactor database queries")
]

priority_queue = []

for task in tasks:
    heapq.heappush(priority_queue, task)

print("Popping tasks in priority order:\n")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Priority {priority}: {task}")