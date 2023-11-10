class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value, value2):
        self.heap.append([value,value2])
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

heap = MinHeap()
a = int(input())
for i in range(a):
    b = int(input())
    c = input()
    heap.insert(b, c)

for i in range(a):
    print(heap.extract()[1])
        