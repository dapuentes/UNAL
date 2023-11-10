class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self.sift_down(0)

        return min_value

    def sift_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest_index][0]:
            smallest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest_index][0]:
            smallest_index = right_child_index

        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self.sift_down(smallest_index)


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

        if value[0] < node.value[0]:
            node.left = self.insert(node.left, value)
        elif value[0] > node.value[0]:
            node.right = self.insert(node.right, value)
        else:
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1 and value[0] < node.left.value[0]:
            return self.rotate_right(node)

        if balance < -1 and value[0] > node.right.value[0]:
            return self.rotate_left(node)

        if balance > 1 and value[0] > node.left.value[0]:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and value[0] < node.right.value[0]:
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

    def pre_order(self):
        results = []

        def traverse(node):
            if node is not None:
                results.append(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return results

    

n = int(input())
heap = MinHeap()
avl_tree = AVLTree()

for i in range(n):
    data = input().split('-')
    name = data[0]
    time = float(data[1])
    heap.insert([time, name])


while heap.heap:
    time, name = heap.extract()
    print(time, name)

    avl_tree.root = avl_tree.insert(avl_tree.root, [time, name])


preorden = avl_tree.pre_order()
for elemento in preorden:
    print(elemento)