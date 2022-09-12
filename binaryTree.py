from typing import *


def main():
    class Node:
        def __init__(self, valueKeyPair: tuple[int, str]):
            self.key = valueKeyPair[0]
            self.value = valueKeyPair[1]
            self.left: Optional[Type[Node]] = None
            self.right: Optional[Type[Node]] = None

    class binaryTree:
        def __init__(self, _node: Optional[Type[Node]] = None):
            self.headNode = _node

        # append another node into binary tree.
            # binary tree is not self balancing.
        def addValueToTree(self, _value: tuple[int, str]):

            if self.headNode is None:
                self.headNode = Node(_value)
            else:
                tmp_node = self.headNode
                while True:
                    if tmp_node.key > _value[0]:
                        if tmp_node.left is None:
                            tmp_node.left = Node(_value)
                            break
                        else:
                            tmp_node = tmp_node.left
                    else:
                        if tmp_node.right is None:
                            tmp_node.right = Node(_value)
                            break
                        else:
                            tmp_node = tmp_node.right
        # append another node into binary tree.
            # binary tree is not self balancing.

        def addNodeToTree(self, _value: Node):

            if self.headNode is None:
                self.headNode = _value
            else:
                tmp_node = self.headNode
                while True:
                    if tmp_node.key > _value.key:
                        if tmp_node.left is None:
                            tmp_node.left = _value
                            break
                        else:
                            tmp_node = tmp_node.left
                    else:
                        if tmp_node.right is None:
                            tmp_node.right = _value
                            break
                        else:
                            tmp_node = tmp_node.right

        # return string value stored in node associated with specific key
        def getValue(self, _key: int) -> Optional[str]:
            tmp_node = self.headNode
            while tmp_node is not None:
                if tmp_node.key == _key:
                    return tmp_node.value
                else:
                    tmp_node = tmp_node.left if tmp_node.key > _key else tmp_node.right
            return None

        # return node associated with specific key
        def getNode(self, _key: int) -> Optional[Type[Node]]:
            tmp_node = self.headNode
            while tmp_node is not None:
                if tmp_node.key == _key:
                    return tmp_node
                else:
                    tmp_node = tmp_node.left if tmp_node.key > _key else tmp_node.right
            return None

        # Count Tree size under a spcific node.
            # This function can be used to count the size of a subtree.
        def countTreeSize(self, _node: Optional[Type[Node]]) -> int:
            if _node is None:
                return 0
            return 1 + self.countTreeSize(_node.left) + self.countTreeSize(_node.right)

        # Count the size of the entire tree starting at the head node.
        def countTotalTreeSize(self) -> int:
            return self.countTreeSize(self.headNode)

    # Code implementation
    b = binaryTree()
    b.addValueToTree((3, "a"))
    b.addValueToTree((4, "b"))
    b.addValueToTree((7, "c"))
    b.addValueToTree((5, "d"))
    b.addValueToTree((2, "e"))

    b.addNodeToTree(Node((1, "f")))

    print(f"Value at {3} is {b.getValue(3)}")
    print(f"Value at {5} is {b.getValue(5)}")
    print(f"Value at {2} is {b.getValue(2)}")
    print(f"Value at {1} is {b.getValue(1)}")

    print(f"Total tree size is: {b.countTotalTreeSize()}")
    print(
        f"Tree size of right subtree is: {b.countTreeSize(b.headNode.right)}")
    print(
        f"Tree size of subtree with head node of key {2} is: {b.countTreeSize(b.getNode(2))}")


if __name__ == "__main__":
    main()
