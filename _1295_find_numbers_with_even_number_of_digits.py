def findNumbers(nums):
    count = 0 
    for num in nums:
        if (check_the_number_of_a_number(num)%2 ==0):
            count +=1
    
    return count

def check_the_number_of_a_number(num):
    count_number = 0
    quotient = num
    while(num!=0):
        num = num // 10
        count_number += 1

    return count_number

if __name__ == "__main__":
    result = findNumbers([12,345,2,6,7896])
    print(result)