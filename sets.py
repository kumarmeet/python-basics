# sets are mutable

names = {"a1", "a2", 5,  "a3", 5}
names1 = {"a4", 5,  "a5", "a6"}

# set does not contain duplicates
print(names)

# get intersection
intersect = names & names1

print(intersect)

#make a union with two sets
mod = names | names1

print(mod)

# difference
mod = names - names1

print(mod)

# check super set of sets

# names has all values in names1
check = names > names1

print(check)

# names1 has all values in names
check = names < names1

print(check)

print(list(names1))

