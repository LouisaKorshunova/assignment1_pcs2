#hea
import heapq
def create_max_heap(arr):
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)    
    return [-heapq.heappop(max_heap) for _ in range(len(max_heap))]

file_path = '/Users/makbuk/Downloads/rosalind_hea.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
arr = [int(i) for i in lines[1].strip().split()]
max_heap = create_max_heap(arr)
max_heap = ' '.join([str(x) for x in max_heap])
print(max_heap)
