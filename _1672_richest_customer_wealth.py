def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    a=[]
    for i in range(len(accounts)):
        a.append(sum(accounts[i]))
    return max(a)

if __name__ == "__main__":
    print(maximumWealth([[1,2,3],[3,2,1]]))