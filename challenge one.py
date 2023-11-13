s=8
arreglo=[]

def crearlista(n):
    for i in range(0,n):
        arreglo.append(i)

def borrar_numeros(arr,s):
    global arreglo
    new_arr=[]

    for ii in range(0,len(arr)):
        for i in range(0,len(arr)):
            if arr[i] > 9:
                num = arr.pop(i)              
                arr.insert(i,int(num/10))
                arr.insert(i+1,num%10)
                break
         
    
    for ii in range(0,len(arr)):
        for i in range(0,len(arr)-1):             
            if arr[i] == s:
                arr.pop(i)
                break

    for i in range(len(arr)-1,0,-1):
        new_arr.append(arr[i])
    arreglo=new_arr


crearlista(s)
borrar_numeros(arreglo,s)
print(arreglo)