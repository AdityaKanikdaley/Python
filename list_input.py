list1 = []
i=0
while(i<10):
    elements = input("Enter Element: ")
    list1.append(elements)
    i+=1
print(list1)

var = input("Enter value to be searched: ")

if(var in list1):
    message = f'\n{var} was found! in list! \n'
    print(message)
else:
    print("Not found!" )