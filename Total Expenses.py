cost=int(input("\n\nEnter the cost per ticket: "))
number=int(input("Enter number of tickets purchased: "))
total=cost*number
if(number<50):
    discounted = total
elif(number>=50 and number<=100):
    discounted = total - (0.1*total)
elif(number>=101 and number<=200):
    discounted = total - (0.2*total)
elif(number>=201 and number<=400):
    discounted = total - (0.3*total)
elif(number>=401 and number<=500):
    discounted = total - (0.1*total)
elif(number>500):
    discounted = total - (0.5*total)
print("Price to be paid: ",discounted, "\n\n")
