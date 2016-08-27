cs=[]
dc=[]
flag=False
while(True):
    number=int(input())
    if(number>0):
        dc=[]
        cs=[]
        counter=0
        flag=False
        for i in range(number):
            cs.append(i+1)
        while(flag==False):
            dc.append(cs.pop(0))
            cs[0]=cs[-1]
            counter+=1
            if(len(cs)==1):
                flag=True
            if(flag==True):
                print(dc)
                break
    elif(number<=0):
        break

    

    


        
    
    

    
    
