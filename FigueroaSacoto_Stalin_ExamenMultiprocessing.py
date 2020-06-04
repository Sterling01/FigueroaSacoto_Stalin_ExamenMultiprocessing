import multiprocessing
import random
import time

def how_many_max_values_sequential(ar):
    #find max value of the list
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]
    print("Numero mayor: ",maxValue)
    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    return contValue

 

# Complete the how_many_max_values_parallel function below.
class productor(multiprocessing.Process, object):
    #Recibir el parametro con el nombre
    def __init__(self, queue, matriz):
        multiprocessing.Process.__init__(self)
        #Asignar dentro de self
        self.matriz=matriz
        self.queue = queue
        
        
    def run(self):
        ac=0
        cant=len(self.matriz)/10
        for i in range(0,10):
            #Agregar el arreglo en porciones a la cola
            self.queue.put(self.matriz[ac:int(ac+cant)])
            #print(self.matriz[ac:int(ac+cant)])
            ac+=int(cant)
     
class consumidor(multiprocessing.Process):
        
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        
    def run(self):
        matMayor=[]
        while True:
            if(self.queue.empty()):
                #print("La cola esta vacia")
                break
            else:
                #Consumir lo que este en la cola en orden FIFO
                item=self.queue.get()
                resultado=getMaxValue(item)
                matMayor.append(resultado)
        #print(matMayor)
        mayorGeneral=getMaxValue(matMayor)
        self.queue.put(mayorGeneral)
         
class final(multiprocessing.Process, object):
    #Recibir el parametro con el nombre
    def __init__(self, queue, matrizFinal):
        multiprocessing.Process.__init__(self)
        #Asignar dentro de self
        self.matriz=matrizFinal
        self.queue = queue
        
        
    def run(self):
        maximo=self.queue.get()
        cont=how_many_max_values_parallel(self.matriz,maximo)
        print("Paralelo: ",cont)
        
def how_many_max_values_parallel(ar,maximo):
    maxValue = maximo
    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    return contValue
    
def getMaxValue(ar):
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]
    return maxValue


 

if __name__ == '__main__':
    #ar_count = 100
    ar_count = 40000000

    #Generate ar_count random numbers between 1 and 30
    ar = [random.randrange(1,30) for i in range(ar_count)]
    print(ar)
    #print(ar[0:10])
    
    inicioSec = time.time()
    resultSec = how_many_max_values_sequential(ar)
    print("Secuencial: ",resultSec)
    finSec =  time.time()
    
    
    inicioPar = time.time()       
    queue=multiprocessing.Queue()
    #Enviar una matriz a un proceso
    procesoProductor = productor(queue,ar) 
    procesoConsumidor = consumidor(queue)
    procesoProductor.start()
    procesoConsumidor.start()
    procesoProductor.join()
    procesoConsumidor.join()
    finPar = time.time() 
    
    procesoFinal= final(queue, ar)
    procesoFinal.start()
    procesoFinal.join()

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))
    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
