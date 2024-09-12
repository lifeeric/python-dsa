from typing import Optional, List


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_node: Optional[Node] = None
        self.right_node: Optional[Node] = None


class Tree:
    def __init__(self) -> None:
        self.root_node: Optional[Node] = None

    def inorder(self) -> None:
        result: List[int] = []
        self._inorder_recursive(self.root_node, result)
        return result

    def _inorder_recursive(self, node, result) -> None:
        if node is None:
            return

        self._inorder_recursive(node.left_node, result)
        result.append(node.data)
        self._inorder_recursive(node.right_node, result)

    def preorder(self) -> None:
        result: List[int] = []
        self._preorder_recursive(self.root_node, result)
        return result

    def _preorder_recursive(self, node: Optional[Node], result) -> None:
        if node is None:
            return None

        result.append(node.data)
        self._preorder_recursive(node.left_node, result)
        self._preorder_recursive(node.right_node, result)

    def postorder(self) -> None:
        result: List[int] = []
        self._postorder_recursive(self.root_node, result)
        return result

    def _postorder_recursive(self, node: Optional[Node], result) -> None:
        if node is None:
            return None
        self._postorder_recursive(node.left_node, result)
        self._postorder_recursive(node.right_node, result)
        result.append(node.data)

    def insert(self, data) -> None:
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            self._insert_recursive(self.root_node, data)

    def _insert_recursive(self, node, data) -> "Node":
        if node is None:
            return Node(data)

        if data < node.data:
            node.left_node = self._insert_recursive(node.left_node, data)
        elif data > node.data:
            node.right_node = self._insert_recursive(node.right_node, data)
        return node

    def search(self, data) -> None:
        return self._search_recursive(self.root_node, data)

    def _search_recursive(self, node, data) -> None:
        if node is None:
            return None
        if node.data == data:
            return node.data

        if data < node.data:
            return self._search_recursive(node.left_node, data)
        return self._search_recursive(node.right_node, data)

    def remove(self, data) -> None:
        self._remove_recursive(self.root_node, data)

    def _remove_recursive(self, node, data) -> None:
        if node is None:
            return node

        if data < node.data:
            node.left_node = self._remove_recursive(node.left_node, data)
        elif data > node.data:
            node.right_node = self._remove_recursive(node.right_node, data)
        else:
            if node.left_node is None:
                return node.right_node
            elif node.right_node is None:
                return node.left_node

            min_node = self._find_min(node.right_node)
            node.data = min_node.data
            self._remove_recursive(node.right_node, min_node.data)

        return node

    def _find_min(self, node) -> Optional[Node]:
        if node.left_node is None:
            return node
        self._find_min(node.left_node)


# n1 = Node("Root Node")
# n2 = Node("Left child")
# n3 = Node("Right child")
# n4 = Node("Left granchild")


# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4

# print(f'{'Inorder':_^40}')
# inorder(n1)
# print(f'{'Preordr':_^40}')
# preorder(n1)
# print(f'{'Postorder':_^40}')
# postorder(n1)


# tree = Tree()

# tree.insert(5)
# tree.insert(4)
# tree.insert(2)
# tree.insert(3)
# tree.insert(1)
# # tree.inorder()
# tree.postorder()

# tree.remove(2)
# tree.search(3)
# tree.inorder()
