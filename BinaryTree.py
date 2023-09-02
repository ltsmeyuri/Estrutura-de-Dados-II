class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        
    def insertLeft(self, value):
        if self.leftchild == None:
            self.leftchild = BinaryTree(value)
        else:
            newnode = BinaryTree(value)
            newnode.leftchild = self.leftchild
            self.leftchild = newnode
            
    def insertRight(self, value):
        if self.rightchild == None:
            self.rightchild = BinaryTree(value)
        else:
            newnode = BinaryTree(value)
            newnode.rightchild = self.rightchild
            self.rightchild = newnode
#Como faço para adicionar no final da árvore?
tree1 = BinaryTree(1)
tree1.insertLeft(2)
