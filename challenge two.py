s=8
arreglo=[6,7,8,9,10,1,2,3,4,5]

def elevar(arr,n):
    global arreglo

    for i in range(0,len(arr)):
        arr.insert(i,pow(arr.pop(i),2))
    
    num=n+(n*10)    
    for i in range(0,len(arr)-1):
        if arr[i] >= num:
            del arr[i]
    
    new_arr=arr 
    num=new_arr[0]
    
    for ii in range (0,len(arr)):
        num=new_arr[ii]
        for i in range(ii,len(new_arr)):     
            #print("new_arr[ii]",new_arr[ii],"new_arr[i]",new_arr[i], "num", num)   
            if new_arr[i]<new_arr[ii] and num > new_arr[i]:
                num=i
            
        try:
            new_arr.insert(ii,new_arr[num])
            del new_arr[num+1]
        except:
            n=0
        
    print(new_arr)


elevar(arreglo,s)

