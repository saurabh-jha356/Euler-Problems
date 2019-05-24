a=1
b=1
c=0
tot = 0
while(c<4000000) :
    c = a + b
    a = b
    b = c
    if(c%2==0) :
         tot += c
print("The total sum of the even valued numbers in fibonacci series till 4000000 is : ",tot)         

    
    
