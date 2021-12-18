def part1(data):
    res = Node.from_list(data[0])
    for d in data[1:]:
        res = add(res, Node.from_list(d))
    return magnitude(res)


def part2(data):
    res = 0
    for d1 in data:
        for d2 in data:
            if d1 != d2:
                res = max(res, magnitude(add(Node.from_list(d1), Node.from_list(d2))))
                res = max(res, magnitude(add(Node.from_list(d2), Node.from_list(d1))))
    return res


class Node:
    def __init__(self, parent=None):
        self.value = None
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return f"[{str(self.left)}, {str(self.right)}]"

    @staticmethod
    def from_list(lst):
        return Node.__from_list_recursive(lst)

    @staticmethod
    def __from_list_recursive(lst):
        node = Node()

        if isinstance(lst, int):
            node.value = lst
            return node

        a, b = lst

        node.left = Node.__from_list_recursive(a)
        node.right = Node.__from_list_recursive(b)

        node.left.parent = node
        node.right.parent = node

        return node


def add(node1, node2):
    node = Node()
    node.left = node1
    node.left.parent = node
    node.right = node2
    node.right.parent = node
    reduce(node)
    return node


def reduce(root_node):
    done = True
    stack = [(root_node, 0)]
    while stack:
        node, depth = stack.pop()

        if node is None:
            continue

        is_exploding = (node.left is not None and node.right is not None) and (
                node.left.value is not None and node.right.value is not None)

        if depth >= 4 and node.value is None and is_exploding:
            # left
            prev_node = node.left
            current_node = node

            while current_node is not None and (current_node.left == prev_node or current_node.left is None):
                prev_node = current_node
                current_node = current_node.parent

            if current_node is not None:
                current_node = current_node.left
                while current_node.value is None:
                    current_node = current_node.right if current_node.right is not None else current_node.left
                current_node.value += node.left.value

            # right
            prev_node = node.right
            current_node = node

            while current_node is not None and (current_node.right == prev_node or current_node.right is None):
                prev_node = current_node
                current_node = current_node.parent

            if current_node is not None:
                current_node = current_node.right
                while current_node.value is None:
                    current_node = current_node.left if current_node.left is not None else current_node.right
                current_node.value += node.right.value

            node.value = 0
            node.left = None
            node.right = None

            done = False
            break

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))

    if not done:
        reduce(root_node)
        return

    stack = [root_node]
    while stack:
        node = stack.pop()
        if node is None:
            continue

        if node.value is not None and node.value >= 10:
            node.left = Node(node)
            node.left.value = node.value // 2
            node.right = Node(node)
            node.right.value = node.value - (node.value // 2)
            node.value = None

            done = False
            break

        stack.append(node.right)
        stack.append(node.left)

    if not done:
        reduce(root_node)


def magnitude(node):

    def __magnitude_rec(current_node):
        if current_node.value is not None:
            return current_node.value
        else:
            return 3 * __magnitude_rec(current_node.left) + 2 * __magnitude_rec(current_node.right)

    return __magnitude_rec(node)



