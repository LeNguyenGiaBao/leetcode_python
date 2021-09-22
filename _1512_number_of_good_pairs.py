def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if(nums[i] == nums[j]):
                count+=1
    
    return count