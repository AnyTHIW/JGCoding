import sys

input = sys.stdin.readline

_N = int(input().rstrip())

class minHeap:
    def __init__(self):
        self.heap = []
        
    def Min_Heapify(self, idx):
        l = self.Left(idx)
        r = self.Right(idx)
        arr = self.heap
        
        if l < len(arr) and arr[l] < arr[idx]:
            smallest = l
        else:
            smallest = idx
            
        if r < len(arr) and arr[r] < arr[smallest]:
            smallest = r
        
        if smallest != idx:
            arr[idx], arr[smallest] = arr[smallest], arr[idx]
            self.Min_Heapify(smallest)
    
    def Build_MinHeap(self):
        arr = self.heap
        
        for i in range(len(arr)//2 - 1, -1, -1):
            self.Min_Heapify(i)
    
    def Adjust_MinHeap(self):
        arr = self.heap
        me = len(arr)-1
        while me > 0 and arr[self.Parent(me)] > arr[me]:
            parent = self.Parent(me)
            arr[parent], arr[me] = arr[me], arr[parent]
            me = parent
            
    
    def append(self, val):
        self.heap.append(val)
        self.Adjust_MinHeap()
        
    def pop(self):
        if self.heap:
            h = self.heap
            
            print(h[0])
            
            if len(h) == 1:
                h.pop()
            else:
                h[0] = h[-1]
                h.pop()
                self.Min_Heapify(0)
            
        else:
            print(0)

    def Parent(self, idx:int):
        return (idx-1) >> 1
    
    def Left(self, idx:int):
        return (idx << 1) | 1
    
    def Right(self, idx:int):
        return (idx << 1) + 2
    
temp = minHeap()

for _ in range(_N):
    
    _X = int(input().rstrip())
    if _X == 0:
        temp.pop()
    else:
        temp.append(_X)
        
