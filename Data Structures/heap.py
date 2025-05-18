# Python only supports min heap by default
# To achieve max heap, just negate the values

import heapq

if __name__ == '__main__':
    min_heap = []
    
    # To insert
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 2)
    heapq.heappush(min_heap, 15)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 500)
    
    # To peek
    smallest = min_heap[0]
    
    # To pop
    smallest = heapq.heappop(min_heap)

    # MAX HEAP
    max_heap = []
    
    # To insert
    arr = [5, 10, 2, 15, 3, 1]
    for elem in arr:
        # negate elem to simulate a max heap
        heapq.heappush(max_heap, -elem)
    
    # To peek
    largest = -max_heap[0]
    
    # To pop
    largest = -heapq.heappop(max_heap)
    
    print('Larget:', largest)
    