import heapq
h = []
for value in [3,6,2,9]:
    heapq.heappush(h, value)
print([heapq.heappop(h) for i in range(len(h))])
