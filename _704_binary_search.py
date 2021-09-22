def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    iLeft = 0
    iRight = len(nums)-1
    while(iLeft<=iRight):
        iMid = (iLeft+iRight)//2
        if(nums[iMid] == target):
            return iMid
        elif (nums[iMid] < target):
            iLeft = iMid+1
        else:
            iRight = iMid-1

    return -1

if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 9))