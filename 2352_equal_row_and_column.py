from collections import Counter

def equal_pairs(grid):
    row_count = Counter(tuple(row) for row in grid)
    count = 0
    for column in zip(*grid):
        count += row_count[column]
    return count

assert(equal_pairs([[3,2,1],[1,7,6],[2,7,7]]) == 1)
assert(equal_pairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3)