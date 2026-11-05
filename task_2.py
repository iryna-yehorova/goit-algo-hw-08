class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_tree_values(root):
    if root is None:
        return 0

    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    print(sum_tree_values(root))  # 35
