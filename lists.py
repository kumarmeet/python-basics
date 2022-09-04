# list can holds different type of values

user_1 = ["Meet", 32, True, {"address": "Bhopal"}]

print(user_1[3]["address"])

string = "abcdefghijkkkkkklmnggtshdgggfossssplaaaqwedmmncgfdrrrtttysssdxxx".count("s")

print("Meet" in user_1)

print(user_1[1: 3])

user_1.append(41)

user_2 = ["hello", "world"]

print(len(user_1))

user_1.extend(user_2)

user_1 += ["it will also works like extend"]

print(user_1)

user_1.remove(41)

print(user_1)

user_1.pop()

print(user_1)

user_1.insert(2,"data")

print(user_1)

user_1[1:1] = ["insert multple 1", "insert multple "]

print(user_1)