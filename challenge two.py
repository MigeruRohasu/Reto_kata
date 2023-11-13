s=8
arreglo=[6,7,8,9,10,2,8,9,10,1,2]
#arreglo=[1,2,3,4,5,6,7,8,9,10,11,12,3,4,5,6,7,8,9,10,11,1,8,9,10,11,12,3,4,5]
def elevar(arr,nn):
    global arreglo

    for i in range(0,len(arr)):
        arr.insert(i,pow(arr.pop(i),2))
    
   

    print(arr)

    new_arr=arr 
    num1=0
    for ii in range (0,len(arr)):

        num1=ii
        for i in range(ii,len(new_arr)):        
            if new_arr[i]<new_arr[ii] and new_arr[num1] > new_arr[i]:
                num1=i
            elif new_arr[i]<new_arr[ii] and new_arr[num1] > new_arr[i]:
                num1=i
        try:
            #new_arr.insert(ii,new_arr[num])
            #del new_arr[num+1]
            new_arr.insert(ii,new_arr.pop(num1))
        except:
            n=0


    print(new_arr)
    num=nn+(nn*10)    
    num1=len(new_arr)
    for i in range(0,num1):   
        for ii in range(0,num1): 
            try:      
                if new_arr[ii] >= num:

                    del new_arr[ii]
            except:
                n=0
      
    print(new_arr)


elevar(arreglo,s)

