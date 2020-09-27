import re

txt = "The rain in Spain falls mainly in the plain"
x = re.findall("aix*", txt)
print(x)

if x:
    print("yes")
else:
    print("No match")

