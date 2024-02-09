#Given n numbers (1 - n), return all possible combinations of size k.(n choose k math problem)
#Time: O(k * 2^n)

def combinations(n, k):
    combs = []
    helper(1, [], n, k)
    return combs

def helper(i, curComb, combs, n ,k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return

    if i > n:
        return
    
    #decision to include i
    curComb.append(i)
    helper(i + 1, curComb, combs, n ,k)
    curComb.pop()

    # decision to NOT include i
    helper(i + 1, curComb, combs, n , k)
    