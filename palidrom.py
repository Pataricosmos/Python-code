i=int( input("Enter number:"))
x=i
rev=0
while(i>0):
      digit = i%10
      rev = rev * 10 + digit 
      i=i//10
if(x==rev):
     print("palidrome number")
else:
    print("not palidrome")
    
