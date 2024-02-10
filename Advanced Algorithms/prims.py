#Prim's Minimum spanning tree
import heapq
def minSpanTree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst, weight in edges:
        adj[src].append([dst, weight])
        adj[dst].append([src, weight])
    
    #Intalize the heap node by choosing a single node
    #(In this case 1) and pushing all its neighbors.
    minHeap = []
    for neighbor, weight in adj[1]:
        heapq.heappop(minHeap, [weight, 1, neighbor])
    print(adj)

    mst = []
    visit = set()
    visit.add(1)
    while minHeap:
        weight, src, node = heapq.heappop(minHeap)
        if node in visit:
            continue

        mst.append([src, node])
        visit.add(node)

        for neighbor, weight in adj[node]:
            if neighbor not in visit:
                heapq.heappop(minHeap, [weight, node, neighbor])
    return mst

