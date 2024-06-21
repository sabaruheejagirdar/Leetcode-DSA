# SORT()
str1 = "ate"

char_list = list(str1)
char_list.sort() #listname.sort()
sorted_str = "".join(char_list) 
print(sorted_str)

# SORTED
str2 = "eating"

sorted_str2= "".join(sorted(str2) )
print(sorted_str2)

# COUNT
nums = [1,1,1,2,2,3,100,110,110];
print(nums.count(3))

freq = [[] for i in range(len(nums)+1)]
print(freq)

str1 = "sabaruhee"
print(str1[1:4])

postfix = [1 for i in range(len(nums))]
print(postfix)
