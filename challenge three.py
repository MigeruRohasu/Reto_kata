#arreglo=[6,7,8,9,10,2,8,9,10,1,2]
#arreglo=[1,2,3,4,5,6,7,8,9,10,11,12,3,4,5,6,7,8,9,10,11,1,8,9,10,11,12,3,4,5]
arreglo=[1,2,4]

def buscar(arr,num):
    flag=False
    for i in arr:
        if i==num:
            flag=True
    
    if flag == False:
        arr.append(num)

    return arr



def crearlista(arr):
    cambio=arr
    for i in range(0,len(arr)):
        cambio=buscar(cambio,arr[i])
    print("cambio", cambio)

    cont=1
    cont1=0
    monedas_restantes=arr
    suma=0
    flag=False
    moneda=0
    while range(0,10):
        while range(0,10):

            for i in monedas_restantes:
                if i == cont:
                    flag=True
            
            monedas_restantes=arr
            try:
                suma=0
                for i in range(cont1,len(monedas_restantes)):
                    print(monedas_restantes,i,suma)
                    suma=suma+monedas_restantes[i]
                    if suma<cont:
                        monedas_restantes.pop(i)
                    if suma == cont:
                        flag=True
            except:
                n=0

            monedas_restantes=arr
            try:
                suma=0
                for i in range(cont1,len(monedas_restantes),-1):
                    print(monedas_restantes,i,suma)
                    suma=suma+monedas_restantes[i]
                    if suma<cont:
                        monedas_restantes.pop(i)
                    if suma == cont:
                        flag=True
            except:
                n=0
            
            print(cont)
            if flag:
                flag=False
                break 
            cont1=cont1+1
        print(cont)
        cont=cont+1
        if flag:
            flag=False
            break                            

    new_arr=cambio 
    num1=0
    for ii in range (0,len(cambio+arr)):
        num1=ii
        for i in range(ii,len(new_arr)):        
            if new_arr[i]<new_arr[ii] and new_arr[num1] > new_arr[i]:
                num1=i
            elif new_arr[i]<new_arr[ii] and new_arr[num1] > new_arr[i]:
                num1=i
        try:
            new_arr.insert(ii,new_arr.pop(num1))
        except:
            n=0
    print(new_arr)
    cambio=[]

    for ii in range(0,len(new_arr)):
        for i in range(ii+1,len(new_arr)):
            try:
                if new_arr[i] == new_arr[ii]:
                    del new_arr[i]
                if  new_arr[i] == new_arr[i+1]:
                    del new_arr[i]
            except:
                n=0        
    print(new_arr)

crearlista(arreglo)