# 2.Solve the Traveling Salesman Problem using DP with bitmasking.
# The Traveling Salesman Problem (TSP) is a classic NP-hard problem. 
# Using Dynamic Programming with Bitmasking, we can solve it in O(n² · 2ⁿ), which is feasible for n ≤ 20.

#####################################        Problem       ##########################################

# We are given n cities and a cost matrix dist[i][j] that gives the distance from city i to city j.
# We need to start at a city (say city 0), visit all cities exactly once, and return to the starting city with minimum cost.

# Solution

import math

def tsp_dp(dist):
    n = len(dist)
    VISITED_ALL = (1 << n) - 1
    
    # dp[mask][i] = min cost to visit all in mask, ending at i
    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[1][0] = 0   # start at city 0
    
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)): 
                continue  # city u not visited
            for v in range(n):
                if mask & (1 << v): 
                    continue  # already visited
                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist[u][v])
    
    # return to start city (0)
    ans = min(dp[VISITED_ALL][i] + dist[i][0] for i in range(1, n))
    return ans


# Example
dist = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]

print("Minimum TSP cost:", tsp_dp(dist))


# Result
# Minimum TSP cost: 97





