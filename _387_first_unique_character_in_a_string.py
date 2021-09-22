def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    
    # 5xxx ms, slow
    # for index, char in enumerate(s):
    #     if s.count(char) == 1:
    #         return index
    # return -1

    list_count = [0]*123
    for i in s:
        list_count[ord(i)]+=1       # ord: convert char to int

    for i, v in enumerate(s):
        if list_count[ord(v)] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(firstUniqChar('leetcode'))