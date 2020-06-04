import time
from mpi4py import MPI
import random

'''
def how_many_max_values_sequential(ar):
    #find max value of the list
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]
    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    return contValue

MatrizFinal = [] 

ar_count = 100
#ar_count = 40000000

#Generate ar_count random numbers between 1 and 30
ar = [random.randrange(1,30) for i in range(ar_count)]
print(ar)
#print(ar[0:10])

inicioSec = time.time()
resultSec = how_many_max_values_sequential(ar)
finSec =  time.time()

print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))
'''

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

matrizMayores = [] 

start = time.time()


if rank == 0:   
    maxValor=0
    #ar_count = 100
    ar_count = 40000000
    #Generate ar_count random numbers between 1 and 30
    ar = [random.randrange(1,30) for i in range(ar_count)]
    print(ar)
    #print(ar[0:10])
    
    ac=0
    cant=int(len(ar)/(size-1))
    for dest in range(1,size):
        comm.send(ar[ac:int(ac+cant)],dest)
        ac+=int(cant)
    
    for i in range(1,size):
        mayorValor=comm.recv(source=i)
        matrizMayores.append(mayorValor)
        #print(extracto)
    for i in range(len(matrizMayores)):
        if i == 0:
            maxValor = matrizMayores[i]
        else:
            if matrizMayores[i] > maxValor:
                maxValor = matrizMayores[i]
    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValor:
            contValue += 1
    print(contValue)
    
    
if rank > 0:
    #print("Proceso ",rank) 
    data=comm.recv(source=0)
    print(data)
    maxValue = 0
    for i in range(len(data)):
        if i == 0:
            maxValue = data[i]
        else:
            if data[i] > maxValue:
                maxValue = data[i]
    print(maxValue)
    comm.send(maxValue,0)
    #print(c)


end = time.time()
'''
print("Tiempo transcurrido: ",end - start)
'''
'''
    print(offse)
    print("\n")
    print(row)
    print("\n")
    print(data)
    print("\n")
    print(data2)
    print("\n")
    '''


'''
    print(averow)
    print("\n")
    print(extra)
'''    
    

'''
    print(Matriz)
    print("\n")
    print(Matriz[0:2])#Matriz desde la fila 0 hasta la 1     

for i in range(size-1):
        comm.send(Matriz, i+1)
        comm.send(Matriz2, i+1)
           
else:
   Matriz = None
   
if rank>0:
    data=comm.recv(source=0)
    data2=comm.recv(source=0)
    print(data)
    print("\n")
    print(data2)
    print("\n")
    
#print("Proceso: %s" %rank+ " recibe el dato: %d" %data)
#print(Matriz)



'''





'''
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
   array_to_share = [1, 2, 3, 4 ,5 ,6 ,7, 8 ,9 ,10] 
           
else:
   array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process = %d" % rank + " variable shared  = %d " % recvbuf )
'''