def credit(n):
    lst=[]
    j=0
    for i in range(len(n)):
        lst.insert(j,n[i])
        j+=1
    i=0
    j=0
    k=1
    l=0
    sum=0
    sum1=0
    for i in range(15):
        if(k>15):
            continue
        j=int(lst[15-k])*2
        if(j<10):
            sum =sum+j
            
        else:
            l=str(j)
            sum1=int(l[0])+int(l[1])
            sum=sum+int(sum1)
            
        k+=2
    
    i=0
    sum2=0
    for i in range(16):
        if(i%2!=0):
            sum2=sum2+int(lst[i])
    
    final=sum+sum2
    
    if(int(final)%10==0):
        print("Valid")
    else:
        print("Not valid")
        
inp=input("Enter card number: ")
credit(inp)
            