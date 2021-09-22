def truncateSentence(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # l = s.split(" ")
    # result =""
    # for i in range(k-1):
    #     result+=l[i]+" "

    # result+=l[k-1]
    # return result

    s+=" "
    result = ""
    count_space = 0
    for i in s:
        if(i==" "):
            count_space+=1
            if(count_space==k):
                return result
        result +=i

if __name__ == "__main__":
    print(truncateSentence("Hello how are you Contestant", 4))
    