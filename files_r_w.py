#%%
# file= open("text.txt","r")
# for line in file:
#    if 'python' in line.lower():
#        print(line)
# file.close()

# print('x'*20)
# print('\n')

# with open('text.txt','r') as file:
#    for line in file:
#       if 'python' in line.lower():    
#         print(line)

# print('x'*20)
# print('\n')

# with open('text.txt','r') as file:
#       line = file.readline()
#       while line:
#          print(line,end="")
#          line = file.readline()

with open('text.txt','r') as file:
   lines_list = file.readlines()
for line in lines_list[::-1]:
   print(line,end="")

