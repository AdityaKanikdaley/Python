#%%
def recursiveFun(n):
    if n<=1:
        return 1
    else:
        a = n * recursiveFun(n-1)
        return a

for i in range(1,10):
    print(i,recursiveFun(i))
# %%
