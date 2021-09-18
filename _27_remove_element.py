def removeElement(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	n = len(nums)
	i=0
	while(i<n):
		print(nums[i], nums)
		if nums[i]== val:
			for j in range(i, n-1):
				nums[j] = nums[j+1]
			n-=1
			i-=1
		i+=1
	return n

def removeElement_2pointers(nums, val):
	k=0
	for i, v in enumerate(nums):
		print(v, nums)
		if v != val:
			nums[k] = nums[i]
			k+=1
	return k

if __name__ == "__main__":
	nums = [0,1,2,2,3,0,4,2]
	val = 2
	print(removeElement_2pointers(nums, val))