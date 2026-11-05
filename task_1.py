class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_min_value(root):
    if root is None:
        raise ValueError("Дерево порожнє")

    current = root
    while current.left is not None:
        current = current.left
    return current.value


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    print(find_min_value(root))  # 2
