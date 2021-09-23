def merge_sort(a, L, R):
    # end condition
    if (L>R):
        return 
    if (L==R):
        return [a[L]]

    # seperate list
    k = int((L+R)/2)

    a1 = merge_sort(a, L, k)
    a2 = merge_sort(a, k+1, R)

    # merge 2 list
    return merge(a1, a2)

def merge(a1, a2):
    i=0
    j=0
    l1=len(a1)
    l2=len(a2)
    result = []

    while(i<l1 and j <l2):
        if(a1[i]<a2[j]):
            result.append(a1[i])
            i+=1
        else: 
            result.append(a2[j])
            j+=1
    
    while(i<l1):
        result.append(a1[i])
        i+=1
    
    while(j<l2):
        result.append(a2[j])
        j+=1
    
    return result

if __name__ == "__main__":
    a = [1,5,3,2,8,7,6,4]
    print(merge_sort(a, 0, len(a)-1))