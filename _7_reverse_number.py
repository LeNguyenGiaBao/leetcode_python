def reverse(x):
    isNev = False
    if(x<0):
        isNev = True
        x = abs(x)
    result = 0
    while(x!=0):
        result = result * 10 + (x%10)
        if result < (-2)**31 or result > 2**31 -1:
            return 0
        x = x//10
    if isNev:
        result = -result
    return result

if __name__ == "__main__":
    print(reverse(1534236469))
    print((-2)**31)
    print(2**31 -1)
    print(1534236469>2**31 -1)