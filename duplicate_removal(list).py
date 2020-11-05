list1 = []
for i in range(10):
    element = input("Enter elements: ")
    list1.append(element)
list1 = list(dict.fromkeys(list1))
 # or use list1 = list(set(list1))
print(list1)

######### f string ########

# a=2
# b=2
# m = f'Aditya is {a} and {b}'
# print(m)