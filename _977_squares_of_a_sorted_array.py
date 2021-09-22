def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return sorted([i*i for i in nums])

if __name__ =="__main__":
    print(sortedSquares([-4,-1,0,3,10]))