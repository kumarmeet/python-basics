#
# tuples allow to immutable objects#

employee = ("samuel", 34, 1254785)

print(employee[0])

print(employee.index(34))

print(34 in employee)

new_tuple = employee + (897546.254, "active")

print(new_tuple)
print(employee)