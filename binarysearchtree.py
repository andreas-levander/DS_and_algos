
class Node:
    def __init__(self, value, leftchild=None, rightchild=None) -> None:
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild

class BST:

    def __init__(self, rootvalue) -> None:
        self.root = Node(rootvalue)

    def add(self, value) -> None:
        def addvalue(node):
            if node == None:
                return Node(value)

            if value < node.value:
                node.leftchild = addvalue(node.leftchild)
                return node

            else:
                node.rightchild = addvalue(node.rightchild)
                return node

        addvalue(self.root)

    def print(self):
        def printvalues(node):
            if node == None:
                return

            printvalues(node.leftchild)
            print(node.value)
            printvalues(node.rightchild)

        printvalues(self.root)

    def search(self, value) -> bool:
        def searchvalue(node) -> bool:
            if node == None:
                return False
            elif node.value == value:
                return True

            elif value < node.value:
                return searchvalue(node.leftchild)

            else:
                return searchvalue(node.rightchild)

        return searchvalue(self.root)

    def delete(self, value) -> None:
        def deletevalue(node):
            if node == None:
                return
            elif node.value == value:
                if node.leftchild == None:
                    return node.rightchild
                elif node.rightchild == None:
                    return node.leftchild
                else:
                    node.rightchild = lift(node.rightchild, node)
                    return node

            elif value < node.value:
                node.leftchild = deletevalue(node.leftchild)
                return node

            else:
                node.rightchild = deletevalue(node.rightchild)
                return node

        def lift(node, deletenode):
            if node.leftchild == None:
                deletenode.value = node.value
                return node.rightchild
            
            else:
                node.leftchild = lift(node.leftchild, deletenode)
                return node

        deletevalue(self.root)
                
        
            



bst = BST(10)
bst.add(5)
bst.add(11)
bst.add(4)
bst.add(7)
bst.add(6)
bst.print()
print(bst.search(11))
bst.delete(5)
bst.print()