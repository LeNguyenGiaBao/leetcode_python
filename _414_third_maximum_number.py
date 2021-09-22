def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_num = [-2**31-1]*3
    for v in nums:
        for i, j in enumerate(max_num):
            if(v==j):
                break
            elif(v<j):
                continue
            else:
                for k in range(len(max_num)-1, i, -1):
                    max_num[k] = max_num[k-1]
                max_num[i] = v
                break
    print(max_num)
    
    if max_num[-1] == -2**31-1:
        return max_num[0]
    return max_num[-1]




if __name__ == "__main__":
    print(thirdMax([2,2,3,1]))