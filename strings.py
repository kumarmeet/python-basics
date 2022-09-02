# only consider new features and syntax, 

# multiline string double or single three quotes
full_name = """
Meet
Kumar
Vishwakarma
"""

print(full_name)

# string methods
print("meet"[0])
print("meet"[-1]) #starts from end
print("mr" in "meet")
print("meet".capitalize())
print("meet".upper())
print("meet".__len__())
print(len("meet"))
print("meet".replace("e","r"))
print("meet".endswith("mt"))
print("meet".isalpha())
print("meet541".isalnum())

#slicing
print("Kumar"[1:3])
print("Kumar"[:3]) #it will start from begining
print("Kumar"[3:]) #it will start from end
print("Kumar is cool"[3:-1]) #ar is coo