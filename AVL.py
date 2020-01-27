class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self):
        self.x = None

    def Insert(self, x, key):
        if x == None:
            return Node(key)
        elif key < x.value:
            x.left = self.Insert(x.left, key)
        else:
            x.right = self.Insert(x.right, key)

        x.height = 1 + max(self.__Height(x.left), self.__Height(x.right))

        # Case: Left-Left
        if self.__Balance(x) > 1 and key < x.left.value:
            return self.Right(x)

        # Case: Right-Right
        elif self.__Balance(x) < -1 and key > x.right.value:
            return self.Left(x)

        # Case: Left-Right
        elif self.__Balance(x) > 1 and key > x.left.value:
            x.left = self.Left(x.left)
            return self.Right(x)

        # Case: Right-Left
        elif self.__Balance(x) < -1 and key < x.right.value:
            x.right = self.Right(x.right)
            return self.Left(x)

        return x

    def Right(self, i):
        z = i.left
        temp = z.right
        z.right = i
        i.left = temp
        i.height = 1 + max(self.__Height(i.left), self.__Height(i.right))
        z.height = 1 + max(self.__Height(z.left), self.__Height(z.right))
        return z

    def Left(self, i):
        z = i.right
        temp = z.left
        z.left = i
        i.right = temp
        i.height = 1 + (max(self.__Height(i.left), self.__Height(i.right)))
        z.height = 1 + max(self.__Height(z.left), self.__Height(z.right))
        return z

    def __Height(self, x):
        if x == None:
            return 0
        return x.height

    def __Balance(self, x):
        if x == None:
            return 0
        return self.__Height(x.left) - self.__Height(x.right)

    def __Min(self, node):
        if node == None:
            raise Exception
        else:
            if node.left == None:
                return node.value
            else:
                return self.__Min(node.left)

    def Delete(self, x, value):

        if x.value == value:
            # leaf case
            if x.left == None and x.right == None:
                return None
            # only right child
            if x.left == None and x.right != None:
                return x.right
            # only left child
            if x.left != None and x.right == None:
                return x.left
        elif value < x.value:
            x.left = self.Delete(x.left, value)
            return x

        elif value > x.value:
            x.right = self.Delete(x.right, value)
            return x

        else:
            if x.left is None:
                node = x.right
                x = None
                return x
            elif x.right is None:
                node = x.left
                x = None
                return x
            node = self.__Min(x.right)
            x.value = node.value
            x.right = self.Delete(x.right, node.value)

        # update the height of the node
        x.height = 1 + max(self.__Height(x.left), self.__Height(x.right))

        # Get the balance factor
        balance = self.__Balance(x)

        # left left rotation
        if balance > 1 and self.__Balance(x.right) >= 0:
            return self.Right(x)

        # right right rotation
        if balance < -1 and self.__Balance(x.right) <= 0:
            return self.Left(x)

        # left right rotation
        if balance > 1 and self.__Balance(x.left) < 0:
            x.left = self.Left(x.left)
            return self.Right(x)

        # Right left rotation
        if balance < -1 and self.__Balance(x.right) > 0:
            x.right = self.Right(x.right)
            return self.Left(x)
        return x

    def PreOrder(self, x):
        if x:
            print(x.value)
            self.PreOrder(x.left)
            self.PreOrder(x.right)

    def PostOrder(self, x):
        if x:
            self.PreOrder(x.left)
            self.PreOrder(x.right)
            print(x.value)

    def InOrder(self, x):
        if x:
            self.PreOrder(x.left)
            print(x.value)
            self.PreOrder(x.right)

def Test():
    avl = AVLTree()

    x = None
    x = avl.Insert(x, 10)
    x = avl.Insert(x, 20)
    x = avl.Insert(x, 30)
    x = avl.Insert(x, 40)
    x = avl.Insert(x, 50)
    x = avl.Insert(x, 25)

    order = input("Enter the order in which you want to view the tree? Select the Number\n1)PreOrder\n2)PostOrder\n3)InOrder\n")
    print("Tree after insertion")
    if order == "1":
        avl.PreOrder(x)
    elif order == "2":
        avl.PostOrder(x)
    elif order == "3":
        avl.InOrder(x)

    print("Tree after deletion")
    avl.Delete(x, 40)
    if order == "1":
        avl.PreOrder(x)
    elif order == "2":
        avl.PostOrder(x)
    elif order == "3":
        avl.InOrder(x)

    return avl

Test()