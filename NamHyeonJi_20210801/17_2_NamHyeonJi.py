def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    res = [0]*len(cost)
    res[0] = cost[0]
    res[1] = cost[1]
    for i in range(2,len(res)):
        res[i] = min(res[i-1], res[i-2]+cost[i])

    return res[len(res)-1]

# cost=[10,15,20]
# print(minCostClimbingStairs(cost))

