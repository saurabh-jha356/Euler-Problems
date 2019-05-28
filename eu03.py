def prime_no(b) :
    print("Prime number function...")
    lim = int(b)/2
    c = 'NP'
    print("i am here...")
    while(int(lim)>=2) :
        if(x%int(lim)==0) :
            c = 'NP'
            return c 
        else :
            c = 'P'
        lim = int(lim) - 1    
    return c ;
#Function ends above

print("Main function....")
a = 600851475143
b = (600851475143/2)
print("this is it..")
print(int(b))
flag = 'NP'
num = 0
while(int(b)>2) :
    print("inside while")
    if(600851475143%int(b)==0) :
        print("la la la la la la ala ala la alalala")
        flag = prime_no(int(b))
        print(flag)
        if(flag=='P') :
            num = int(b)
            break
            #return 0
        else :
            b = int(b) - 1
    b = int(b) - 1
    print(int(b))
print("The largest prime factor of 600851475143 is : ",num)
print("Thankyou for using my program..")    
