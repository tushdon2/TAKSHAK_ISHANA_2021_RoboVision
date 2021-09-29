import math

class Pixel:
    # Class to store pixel properties
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.parent_row = None
        self.parent_col = None
        self.queueIndex = None

        # for Dijkstra's Algorithm
        self.visited = False 
        self.dist = math.inf
        self.neighbours = []

class PriorityQueue:
    # Data Structure for Priority Queue (Min-Heap) for Dijkstra's Algorithm
    def __init__(self, pixMtrx):
        self.__queue = [] # list as min-heap (aka Priority Queue)
        self.length = 0 # number of nodes/objects in the heap
        # dequeue from index 0 and enqueue from last index
        # Heap node with index i in queue has children with indices: (2 * i + 1) for left and (2 * i + 2) for right
        # Heap node with index i in queue has parent with index (i//2 - 1)
        
        for _ in pixMtrx:
            # pixMtrx is a 2D array containing Pixel objects for white pixels
            for obj in _:
                if obj != None:
                    # adding objects to the queue, order doesn't matter
                    obj.queueIndex = self.length # setting the index of pixel in the queue
                    self.__queue.append(obj) 
                    self.length += 1

        # Building the heap, from starting index to first index of queue
        # start index = length//2 - 1
        self.buildHeap(self.length//2 - 1)

    def swap(self, index1, index2):
        self.__queue[index1], self.__queue[index2] = self.__queue[index2], self.__queue[index1]
        self.__queue[index1].queueIndex = index1
        self.__queue[index2].queueIndex = index2

    def __heapify(self, index):
        smallest = index # initialising index as smallest
        l = 2 * index + 1
        r = l + 1

        if l < self.length and self.__queue[l].dist < self.__queue[smallest].dist: 
            smallest = l
        if r < self.length and self.__queue[r].dist < self.__queue[smallest].dist: 
            smallest = r

        if smallest != index:
            self.swap(index, smallest)
            self.__heapify(smallest) # recursive function call
    
    def buildHeap(self, index):
        for i in range(index, -1, -1):
            self.__heapify(i)

    def dequeue(self):
        # Technically, while dequeuing from front, the first element is swapped with the last, and then removed from the end
        # Still need to build the heap to maintain the heap property in the queue, it has to be done manually after changing the pixel properties
        item = self.__queue[0]
        self.swap(0, self.length - 1)
        self.__queue.pop()
        self.length -= 1
        return item