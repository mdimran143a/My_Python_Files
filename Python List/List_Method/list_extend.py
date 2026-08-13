# Extend in Python

number = [1,2,3,4,5]
tp_number = (11,12,13,14,15)
number.extend([6,7,8,9,10])
number.extend(tp_number)

for i in number:
    print("List Items : ", i)


print("The list of Numbers : ", number)