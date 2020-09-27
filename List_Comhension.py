# num = [1,2,3,4,5,6,7,8,9]
# sqr_num = []

# for x in num:
#     sqr_num.append(x**2)
# print(sqr_num)

########################## List Comprehension ######################

# sqr_num1 = [x**2 for x in num]
# print(sqr_num1)



# name = []
# for letter in 'Aditya':
#     name.append(letter)
# print(name)



# name1 = [letter for letter in 'Aditya']
# print(name1)

###################### Conditional List Comprehention #############################

# even = []
# for x in range(10):
#     if x%2==0:
#         even.append(x)
# print(even)


# even1 =[x**2 for x in range(10) if x%2==0]
# print(even1)
# # x is expression
# # for x in range(10) is loop
# # if(x%2==0) is condition


###################### Nesting List Comprehension ######################

# my_list = []
# for x in [2,4,6]:
#    for y in [1,3,5]:
#        my_list.append(x*y)
# print(my_list)

# # nested loop
# my_list1 = [x*y for x in [2,4,6] for y in [1,3,5]]
# print(my_list1)

# # nested if
# my_list1 = [x*y for x in [2,4,6] for y in [1,3,5] if x*y != 10 if x*y != 20 ]
# print(my_list1)



###################### else in List Comprehension ######################

list_ = [['a','b','c'], ['d','e','f'], ['g','h','i']]

list1 = []
for x in list_:
    if 'g' not in x:
        list1.append(x)
    else:
        list1.append('Letter was skipped')
print(list1)


list_sc = [x for x in list_  if 'g' not in x]
print(list_sc)

# now sing else
list_sc = [x  if 'g' not in x else 'Letter was skipped' for x in list_ ]
print(list_sc)
