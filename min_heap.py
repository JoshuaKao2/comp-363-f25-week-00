class MinHeap:
    
    def __init__(self):
        self.heap = []


    def add(self, value):
        self.heap.append(value)
        self.swap_up(len(self.heap) - 1)


    def remove(self):
        result = None
        if len(self.heap) == 1:
            result = self.heap.pop()
        elif len(self.heap) > 1:
            result = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.swap_down(0)
        return result



    def swap_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.swap(self.heap, parent, index)
                index = parent
            else:
                index = 0  



    def swap_down(self, index):
        size = len(self.heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < size and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < size and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                index = size            


    def swap(self, i: int, j: int) -> None:
        if i != j:
            temp = self.heap[i]
            self.heap[i] = self.heap[j]
            self.heap[j] = temp

    def size(self):
        return len(self.heap)
    
    def min_val(self):
        value = None
        if self.heap:
            value = self.heap[0]  
        return value