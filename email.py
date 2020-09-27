string = input("Enter names")
name_list = string.split(' ')
print(name_list)
dictionary={}
for name in name_list:
    email=input("Enter email for "+ name+" ")
    dictionary[name] = email
print(dictionary)
