def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # new_number = 0
    # old_number = x
    # if(x<0):
    #     return False
    # while (x!=0):
    #     new_number = new_number*10 + int(x%10)
    #     x = int(x/10)
    # return new_number == old_number

    return str(x) == str(x)[::-1] # faster

if __name__ == "__main__":
    print(isPalindrome(121))