s = "test string"
dict = {}
for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i,j in dict.items():
    if j > 1:
        print(f"{i}, count = {j}")