#%%
# def num(*args):
#     print(args)
#     print("1 " + args[0] + " 2")
#     print("3 " + args[1] + " 4")
#     print("5 " + args[2] + " 6")

# num('hii','shii','suuu','aditya')

def sum(*args):
    print(args)
    result = 0
    for x in args:
        result +=x
    print(result) 
    
sum(1,2)

# %%
