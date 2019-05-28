def palin(num) :
    num1 = 0
    palin_flag = 'N'
    num1 = num
    palin_num=0
    while(int(num1)>0) :
        rem = int(num1%10)
      #  print(int(rem))
        num1 = int(num1/10)
      #  print(num1)
        palin_num= palin_num*10 + int(rem)
      # print(palin_num)
    #print("The num in the function is : ",num)
    #print("The palin_num in the function is : ",palin_num)
    if(num==palin_num) :
        palin_flag = 'Y'
    return palin_flag ;


i = 999
j = 999
num = 0
p_flag = 'N'
while(i>99 and p_flag=='N') :
    j = 999
    while(j>99 and p_flag == 'N') :
        num = i*j
        print(i,"*",j,"=",i*j)
        p_flag = palin(num)
        j = j-1
        print("Flag = ",p_flag)
        if(p_flag=='Y') :
            print("Palindrome is : ",num) 
    i=i-1        
print("Thankyou for using my program.......")

                
                
        
        
           
