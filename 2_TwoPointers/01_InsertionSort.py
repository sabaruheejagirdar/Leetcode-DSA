def insertion_sort(nums):

    for i in range(1,len(nums)):
        j = i-1

        while(j>=0 and nums[j+1]<nums[j]):
            # swap
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp

            j-=1

    return nums


nums = [2,3,4,1,6]
output = insertion_sort(nums)
print(output)


# i=1 # [2,3,4,1,6]
# i=2 # [2,3,4,1,6]
# i=3 # [2,3,4,1,6]
###### [2,3,1,4,6]
###### [2,1,3,4,6]
###### [1,2,3,4,6]
# i=4 # [1,2,3,4,6]