
t=0
t=int(input("tapper 1 pour lancer le programme avec while."))
if (t==1):
    print("vous lancez le programme avec while")
else:
    print("vous lancez le programme avec for")

a=int(input("enter the number : "))
result = 1
i=1

if(t==1):
   while(i <= a):
    result=i*result
    i=i+1

else:
    for i in range(1, a + 1):
     result *= i



print("factorielle est  égale a  ", result)
