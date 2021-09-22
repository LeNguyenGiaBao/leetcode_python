def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    m = len(word1)
    n = len(word2)
    w1=w2=""
    for i in range(m):
        w1 += word1[i]
    for i in range(n):
        w2 += word2[i]
    return w1==w2

if __name__ == "__main__":
    print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))