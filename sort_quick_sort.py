def quick_sort(a, L, R):
    if L>=R:
        return a

    # Step 1. choose key
    key = a[int((L+R)/2)]

    # Step 2. allocate the list
    k = partition(a, L, R, key)

    # Step 3. Seperate the list
    quick_sort(a, L, k-1)
    quick_sort(a, k, R)

# return the pivot. The pivot is the firt index of the right-child list, use to seperate into 2 child list
def partition(a, L, R, key):
    aL = L
    aR = R
    
    while(aL<=aR):
        while(a[aL] < key):
            aL+=1

        while(a[aR] > key):
            aR-=1

        if (aL <= aR):
            temp = a[aL]
            a[aL] = a[aR]
            a[aR] = temp

            aL+=1
            aR-=1
        
    return aL

if __name__ =="__main__":
    a = [0]
    quick_sort(a, 0, len(a)-1)
    print(a)
    