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
    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    return contValue

 

# Complete the how_many_max_values_parallel function below.
def how_many_max_values_parallel(ar):
    
    '''
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
    '''
    return 0
 

if __name__ == '__main__':
    ar_count = 100
    #ar_count = 40000000

    #Generate ar_count random numbers between 1 and 30
    ar = [random.randrange(1,30) for i in range(ar_count)]
    print(ar)
    print(ar[0:10])
    
    pool = multiprocessing.Pool(processes=10)
    cant = (ar_count/10)
    acum=0
    for i in range(0,10):
        print("Desde ",acum, "hasta ", acum+cant)
        acum+=cant
        #pool_outputs = pool.map(how_many_max_values_parallel, ar[])
        
    #pool.close() 
    #pool.join()      
    
    #print ('Pool    :', pool_outputs)    

    inicioSec = time.time()
    resultSec = how_many_max_values_sequential(ar)
    finSec =  time.time()

    inicioPar = time.time()   
    resultPar = how_many_max_values_parallel(ar)
    finPar = time.time()     

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
