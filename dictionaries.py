#dictionaries allows multiple key value pairs

employee = {"name":"susane", "age":25, "salary": 23655241258}

copy_emp = employee.copy()

print(employee)

#checks key in dict
print("name" in employee)

employee["age"] = 24

print(employee)

print(employee.get("salary", "name"))

employee.pop("age")
print(employee)

#remove the last key value
employee.popitem()
print(employee)

print(list(copy_emp.keys()))
print(list(copy_emp.values()))

# convert dict into lists

print(list(copy_emp.items()))

copy_emp["new address"] = "Ireland"

print(copy_emp)

del copy_emp["name"]

print(copy_emp)