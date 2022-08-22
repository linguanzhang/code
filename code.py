import random
a=random.randint(1,100)
msg='guess from{}~{}'
minnum=1
maxnum=100
c=True

while c:
    b=int(input(msg.format(minnum,maxnum)))  
    
        
    
   
    if b>a:
        print('smaller')
        maxnum=b
        if b>100:
            maxnum=100
            print('please enter between 1~100')
        
    elif b<a:
        print('larger')
        minnum=b
        if b<1:
            minnum=1
            print('please enter between 1~100')
    elif b==a:
        print('correct')
        c=False


#if b>100:
       # print('what are you doing?')
#elif b<1:
       # print('what are you doing?')

         
        
        
    
