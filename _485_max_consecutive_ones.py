def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    max_count = 0
    for i in nums:
        if(i==1): 
            count+=1
            if(count>max_count):
                max_count = count
        else: 
            count = 0
    return max_count

if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1,0,1,1,0,1]))