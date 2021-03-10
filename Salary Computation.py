#%%
basic=float(input("\n\nEnter your basic salary: "))
if(basic<15000):
    HRA = (0.15*basic)
    DA = (0.9*basic)
elif(basic>=15000):
    HRA = 5000
    DA = (0.98*basic)

gross = basic+HRA+DA
print("Your gross salary is:",round(gross,2),"\n\n") 
# %%
