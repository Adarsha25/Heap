import heapq

# initializing list
a = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(a)

# printing created heap
print("The created heap is : ", end="")
print(list(a))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(a, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(a))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(a))