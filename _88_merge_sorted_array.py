def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    # l = m+n
    # for v2 in nums2:
    #     findK = False
    #     for i, v in enumerate(nums1):
    #         if v2 <v:
    #             findK = True
    #             for j in range(l-1, i, -1):
    #                 print("j", j, "i ", i)
    #                 nums1[j] = nums1[j-1]
    #             nums1[i] = v2
    #             m+=1
    #             break
    #     if not findK:
    #         nums1[m] = v2
    #         m +=1
    # print(nums1)

    # 2 pointers
    # l = m + n
    # i = m-1
    # j = n-1
    # for k in range(l-1, -1, -1):
    #     if(i>=0 and j>=0):
    #         if (nums1[i] > nums2[j]):
    #             nums1[k] = nums1[i]
    #             i-=1
    #         else:
    #             nums1[k] =nums2[j]
    #             j-=1
    #     elif(i>=0):
    #         nums1[k] = nums1[i]
    #         i-=1
    #     elif(j>=0):
    #         nums1[k] = nums2[j]
    #         j-=1
    # print(nums1) 

    # using sort fuction
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    print(nums1)

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0] 
    m = 3 
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
