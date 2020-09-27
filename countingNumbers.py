l1 = []
for i in range(20):
    elements = int(input("Enter 20 elements:"))
    l1.append(elements)
positiveCount=0
negativeCount=0
oddCount=0
evenCount=0

for num in l1:
    if(num>0):
        positiveCount+=1
    if(num<0):
        negativeCount+=1 
    if(num%2!=0):
        oddCount+=1
    if(num%2==0):
        evenCount+=1   

print("Positives: ",positiveCount)
print("Negatives: ",negativeCount)
print("Odds: ",oddCount)
print("Evens: ",evenCount)
print("Zeros: ",l1.count(0))


