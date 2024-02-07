#Count the number of unique paths from the top left to bottom right.
#You are only allowed to move down or to the right. 

#Brute Force Time and Space complextity O(2^(n + m))
def bruteforce(r,c,rows,cols):
    if r ==rows or c == cols:
        return 0
    if r == rows-1 and c==cols-1:
        return 1
    
    return (bruteforce(r + 1, c, rows, cols) +
            bruteforce(r, c + 1, rows, cols))
bruteforce(0, 0, 4, 4)

# Memorization Time and Space Complexity O(n * m): [We can try cache and hashmap as well]
def memorization(r, c, rows, cols, cache):
    if r ==rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    
    if r == rows-1 and c == cols-1:
        return 1
    cache[r][c] = memorization(r+1, c, rows, cols, cache) + memorization(r, c+1 + rows + cols)
    return cache[r][c]

memorization(0, 0, 4, 4, [[0]*4 for i in range(4)])


# Dynamic Programming Time O(n * m), Space O(m), where m is no of cols
def dp(rows, cols):
    prevRow = [0] * cols

    for r in range(rows-1, -1, -1):
        currRow = [0] * cols
        currRow[cols -1] = 1
        for c in range(cols - 2, -1, -1):
            currRow[c] = currRow[c+1] + prevRow[c]
        prevRow = currRow
    return prevRow[0]

print(dp(4, 4))