show1=int(input("Enter the number of people who watched show 1:  "))
avg1=float(input("Enter the average rating for show 1:  "))

show2=int(input("Enter the number of people who watched show 2:  "))
avg2=float(input("Enter the average rating for show 2:  "))

show3=int(input("Enter the number of people who watched show 3:  "))
avg3=float(input("Enter the average rating for show 3:  "))

sum=(avg1+avg2+avg3)/3

print("\n\nThe overall average rating for the show is:" , round(sum,2) , "\n\n")

