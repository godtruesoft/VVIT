a = 4
b = 3
c = 2

D = b*b - 4*a*c
if D>0:
    x1 = (-b + D**(1/2))/(2*a)
    x2 = (-b - D**(1/2))/(2*a)
    print ("First ",x1) 
    print ("Second ",x2)
elif D==0:
    x = (-b)/(2*a)
    print("Answer: ",x)
else:
    print("No answer")