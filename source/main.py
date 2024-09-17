class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def min_depth(root):
    if root is None:
        return 0

    queue = [(root, 1)]
    while queue:
        node, depth = queue.pop(0)

        if node.left is None and node.right is None:
            return depth

        if node.left is not None:
            queue.append((node.left, depth + 1))

        if node.right is not None:
            queue.append((node.right, depth + 1))


graph = {}
with open("input.txt", "r") as file:
    root = Node(int(file.readline()))
    graph[root.value] = root
    for line in file:
        parent, child = map(int, line.split(","))
        if parent not in graph:
            graph[parent] = Node(parent)
        if child not in graph:
            graph[child] = Node(child)
        if graph[parent].left is None:
            graph[parent].left = graph[child]
        else:
            graph[parent].right = graph[child]


with open("output.txt", "w") as file:
    file.write(str(min_depth(root)))
