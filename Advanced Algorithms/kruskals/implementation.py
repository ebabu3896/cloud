#First learn union algorithm

#Given an list of edges of a connected undirected graph with nodes numbered from 1 to n,
#Return a list edges making up to min spanning tree.
import heapq
def minSpanTree(edges, n):
    minHeap = []
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, [weight, n1, n2])
    
    unionFind = unionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)
        if not unionFind.union(n1, n2)
            continue
        mst.append([n1, n2])
    return mst