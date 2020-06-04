# Examen Computacion Paralela
1. Multiprocessing <br />
Se tiene un proceso productor, consumidor, y final. El proceso productor recibe el arreglo generado y agrega a la cola partes de este, para que los demas procesos consuman los items desde la cola.
El proceso consumidor ocupa los items(partes del arreglo) que estén en la cola y cada item recuperado lo envia a un metodo que retorna el mayor valor ese item. Como el arreglo general fue dividido se tiene que formar un nuevo arreglo con los valores mayores por cada item.
Este nuevo arreglo es enviado a un nuevo proceso llamado procesoFinal que envia a un metodo el arreglo general y el maximo valor obtenido que cuenta las veces que el numero mayor de todo el arreglo general se repite en el mismo.<br /><h6>Definir los procesos</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im1.png)<br /><h6>Proceso Productor</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im2.png)<br /><h6>Proceso Consumidor</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im3.png)<br /><h6>Proceso Final</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im4.png)<br /><h6>Metodos</h6>
El primer metodo recibe como parametros el arreglo general y el maximo valor obtenido para realizar el conteo de las veces que se repite en arreglo inicial<br />
El segundo metodo recibe como parametro una seccion del arreglo y de esa seccion obtiene el maximo valor.
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im5.png)<br /><h6>Resultados</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im6.png)<br />

2. MPI <br />
Si el id del proceso es 0 este se encargara de generar el arreglo para despues haciendo uso de un bucle enviar a los procesos restantes secciones del arreglo generado, luego los procesos con id mayor a 1 reciben los datos y por cada seccion del arreglo recuperado obtienen el maximo valor solo de esa seccion
y este valor obtenido es nuevamente enviado al proceso 0, que en un nuevo arreglo recopila los resultados de las secciones del arreglo inicial, para obtener el maximo valor final y asi en base a este valor obtener cuantas veces se repite en el arreglo inicial<br /><h6>Proceso 0</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im1_1.png)<br /><h6>Procesos restantes</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im1_2.png)<br /><h6>Resultado</h6>
![alt text](https://github.com/Sterling01/Practica01-MiBlog/blob/master/images/im1_3.png)<br />

<strong>Como correr FigueroaSacoto_Stalin_ExamenMPI.py </strong><br />
mpiexec -n 11 python3 FigueroaSacoto_Stalin_ExamenMPI.py
