print("This program calculates the total of multiples of 3 and 5 from 1 to 1000")
total = 0
for x in range(1,999) :
    if(x%3==0 or x%5==0) :
        total += x

print("The total is : ",total)        
