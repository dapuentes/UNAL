class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):        
        self.root = None

    def insert(self, node, value):
        if self.root is None:
            node = Node(value)
            self.root = node
            return node

        if not node:            
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            
        balance = self.get_balance(node)                    
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
            
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
            
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
            
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        if node == self.root:
            self.root = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        if node == self.root:
            self.root = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def delete(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                suc = self.find_successor(node.right)
                node.value = suc.value
                node.right = self.delete(node.right, suc.value)

        if not node:
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node  

    def find_successor(self, node):
        while node.left:
            node = node.left
        return node

    def in_order(self):
        results = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            results.append([node.value, node.height])
            if node.right is not None:
                traverse(node.right)

        traverse(self.root)
        return results

    def in_order_reverse(self):
        aux = []

        def traverse(node):
            if node.right is not None:
                traverse(node.right)
            aux.append(str(node.value))
            if node.left is not None:
                traverse(node.left)

        traverse(self.root)
        return " ".join(aux)

    def is_complete(self):
        def is_complete_recursive(node, index, aux):
            if node is None:
                return True

            if index >= aux:
                return False

            return (is_complete_recursive(node.left, 2 * index + 1, aux) and
                    is_complete_recursive(node.right, 2 * index + 2, aux))

        aux = self.count_nodes(self.root)
        return is_complete_recursive(self.root, 0, aux)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def is_full(self):
        def is_full_recursive(node):
            if node is None:
                return True

            if node.left is None and node.right is None:
                return True

            if node.left is not None and node.right is not None:
                return (is_full_recursive(node.left) and is_full_recursive(node.right))

            return False

        return is_full_recursive(self.root)

    def is_perfect(self):
        return self.is_complete() and self.is_full()

tree = AVLTree()
a = int(input())

for _ in range(a):
    b = int(input())
    tree.insert(tree.root, b)

if tree.is_perfect() == True:
    print("el arbol es perfecto")
elif tree.is_full() == True:
    print("el arbol esta lleno")
elif tree.is_complete() == True:
    print("el arbol es completo")
elif tree.is_perfect() == False:
    print("el arbol no es completo ni esta lleno") 


print(tree.in_order_reverse())

