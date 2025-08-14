# Heaps
import heapq

# Build heap from inital values in array
arr = [1, 5, 2, 4, 19, 7]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))