nums = [15,5,3,16,9,83,7,5,12,48,95]
nums.sort()
print(nums)

names = ["Bob", "Rune", "Jackob", "amity"]

#copy one list to another
names_copy = names[:]

names.sort()
print(names)

# by default upper case list consider 
# first in sorting even in the list has 
# words starts with a after B
# in this case use below statement

names.sort(key=str.lower)
print(names)
print(names_copy)

#want to not change in original list and sort return a new list
print(sorted(names, key=str.lower))


