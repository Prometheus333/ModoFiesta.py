#Esta es la biblioteca extra que he investigado

#utilizado para ayudar al usuario a agendar su reunion en modo fiesta

#datetime toma la fecha y hora exacta del sistema

#con ella puede ser impresa cruda

#tambien puede ser manipulada para agendar

# como agregar dias o quitar dias 

import datetime

#Aqui solamente estoy imprimiendo la fecha y hora del dia de hoy

# Ayuda a que el usuario pueda observar la diferencia de fechas

print(datetime.datetime.now())

#esta es la primera parte del proyecto

#ayuda al usuario a cuidar su tiempo mientras esta en netflix

#empezamos preguntandeole al usuario si puede ingresar la informacion 

#Simple recopilacion de datos para no sobrepasar el limite de caracteres

def horas_totales():
    
    A_horas= "¡Hola! este programa te ayuda "
    
    B_horas= "a organizar el tiempo que utilizas en Netlix "
    
    C_horas= "¿cuantas horas planeas estar en Netflix?"
    
    return (A_horas, B_horas, C_horas)

#Cuando el usuario conteste toda la informacion

#se utiliza para poder obtener el tiempo en el que ha estado viendo Netflix

print(horas_totales())

horas=float(input())

def tiempo_total():
    
    A_tiempo= "Ingresa la duracion de uno de los episodios "
    
    B_tiempo= "que estas viendo(minutos) "
    
    return (A_tiempo, B_tiempo)

print(tiempo_total())

tiempo=float(input())

A_episodios= ("Gracias ahora ingrese el numero de episodios que ha visto")

print(A_episodios)

episodios=int(input())

#Aqui empieza el bucle while

#es evitar que el usuario sea capaz de ingresar numeros negativos

#De esta manera el programa puede funcionar correctamente.

while (horas < 0):
    
    print:"error, debe ser un numero positivo"
    
    horas=float(input("(error, debe ser positivo)", C_horas))
    
while (tiempo < 0):
    
    print:"error, debe ser un numero positivo"
    
    tiempo=float(input("(error, debe ser positivo)", A_tiempo))
    
while (episodios < 0):
    
    print:"error, debe ser un numero positivo"
    
    episodios=int(input("(error, debe ser positivo)", A_episodios))
    
#Esta es la funcion para transformar los episodios en horas totales
    
#para que en la siguiente funcion condicional
    
#se pueda entender llegar facilmente a los limites impuestos por el usuario

def minutos(a,b):
    
    return a * b / 60

res=(minutos(episodios,tiempo))

# iniciamos la condicional

#de tal manera que le diga al usuario si sigue en tiempo o no

if(res < horas):
    
    print("No has excedido tu limite de tiempo :)")
    
#esta es la siguiente toma de decisiones en elif
    
#toma en cuenta como el resultado es igual a horas
    
#eso significa que el usuario esta llegando al limite que el mismo ha puesto
    
elif(res == horas):
    
   print("Estas a punto de excederte, ¿que tal si nos detenemos un tiempo?")
   
#finalmente se agrega un else al final
   
#aclara que el usuario se ha excedido
   
else:
    
    print("¡¡Detente!! has excedido tu limite de tiempo")

#este es un nuevo modo implementado con listas para el usuario
    
modo_fiesta=str(input("¿Deseas entrar en modo fiesta? (si)(no)(info)"))

#iniciamos con condicional para dar opcion al usuario de que hacer

#la primera es solo otorgar informacion

if modo_fiesta == "info" or modo_fiesta == "Info":
    
    def info_total():
        
        A_info= "Modo fiesta es una extension de ayuda "
        
        B_info= "para facilitar la organizacion de los invitados "
        
        C_info= "en caso de hacer una reunion :)"
        
        return (A_info, B_info, C_info)
    
    print(info_total())
    
    modo_fiesta=str(input("¿Deseas entrar en modo fiesta? (si)(no)"))
    
#la segunda es en caso de resultado negativo
    
if modo_fiesta == "no" or modo_fiesta == "No":
    print("Gracias por utilizarme")
    
#esta es la tercera que es la positiva
    
#se trabaja la mayor parte con ciclos, listas, biblioteca, etc.
    
elif modo_fiesta == "si" or modo_fiesta == "Si":
    
#Aqui es la variable de la biblioteca de python
    
#sirve para que el programa grabe que dia es hoy
    
    hoy=datetime.date.today()
    
#Aqui le pide al usuario que ingresee el numero de dias para la reunion 
    
    dias=int(input("¿Cuantos dias faltan para la reunion?"))
    
#Con los dias que ha ingresado el usuario, se crea la funcion time delta
    
#con time delta la variable que fue ingresada por el usuario
    
#es capaz de afectar la fecha 
    
    ultdia=datetime.timedelta(days=dias)
    
#se introduce una lista vacia
    
#con el ciclo de for se va a llenar hasta cinco espacios
    
#segun la comida que ingrese el usuario 
    
    lista=[]
    
#Este es un acumulador externo al ciclo (para que los datos no se borren)
    
    r=5
    
#este es un bucle for para insertar los datos necesarios en la lista vacia
    
    for k in range (0,5):
        
        com=str(input("introduce opciones de comida para invitados"))
        
#En esta parte he utilizado r para no acumular
        
# Si no para borrar el espacio usado por el usuario
        
        r-=1
        
        print("quedan",r," espacios")
        
        lista.insert(k, com)
        
    print("Listo, ahora")
    
#Esta es la siguiente lista vacia con la que se llenara con bebidas
    
#con el mismo ciclo for hasta 5 espacios
    
# es exactamente igual al anterior pero con variables distintas
    
    lista2=[]
    
    f=5
    
    for w in range (0,5):
        
        beb=str(input("introduce opciones de bebidas para invitados"))
        
        f-=1
        
        print("quedan", f," espacios")
        
        lista2.insert(w, beb)
        
#La lista anidada sera la opcion de escoger dos generos de peliculas 
    
    matriz=[["terror","suspenso"],["comedia","stand up"],
            ["drama","romance"],["accion","hollywood"]]
    
#Este es el input de agregar invitado 
    
    inicio=str(input("Agregamos a algun invitado? (si)(no)"))
    
#estos son los contadores y acumuladores para el ciclo
    
#para registrar los inputs por medio externo del ciclo
    acum=0
    
    cont= ""
    
#se agrego la condicional de detenerse o seguir
    
    if inicio=="no" or inicio=="No":
        
        print("no agregaste a nadie, ¿no tienes amigos? :(")
        
#Aqui inicia el ciclo principal para el modo fiesta    
    
        
    while inicio=="si" or inicio=="Si":
        
#Inicia con una bienvenida        
        
        nombre=(str(input("Hola, ¿Como te llamas?")))
        
#este es un acumulador para ver cuantas personas han sido ingresadas
        
        acum += 1
        
        print("Hola ", nombre)
        
#se imprime la lista para que el usuario pueda ver el "menu"
        
        print(lista)
        
#se le ofrece al usuario las opciones para organizar al huesped de la reunion
        def Opcion_1():
            
            A_Opcion1="¿Que te gustaria comer mientra ves peliculas "
            
            B_Opcion1="de estas opciones? (0)(1)(2)(3)(4)"
            
            return (A_Opcion1, B_Opcion1)
        
        opcion1= int(input(Opcion_1()))
        
        print(lista2)
        
        def Opcion_2():
            
            A_Opcion2="¿Que te gustaria beber mientra ves peliculas "
            
            B_Opcion2="de estas opciones? (0)(1)(2)(3)(4)"
            
            return (A_Opcion2, B_Opcion2)
        
        opcion2= int(input(Opcion_2()))
        
        print(matriz)
        
#tambien se le ofrecen las opciones de que peliculas le interesan
        
        def Opcion_3():
            
            A_Opcion3="¿Que generos te gustaria ver "
            
            B_Opcion3="de estas opciones? (0)(1)(2)(3)"
            
            return (A_Opcion3, B_Opcion3)
        
        opcion3= int(input(Opcion_3()))
        
#esto es para organizar y facilitar mandarlo al shell
        
        comer= "escogió comer", lista[opcion1]
        
        beber= "escogió beber", lista2[opcion2]
        
        ver= "y ver", matriz[opcion3]
        
        decision=nombre, comer, beber, ver
        
        print(decision)
        
#Esta es la ultima acumulacion del ciclo para el print
        
        cont= cont, decision 
        
        inicio=str(input("Deseas agregar a mas personas? (si)(no)"))
        
#este es el final y se agrupan toda la informacion para el huesped
        
        if inicio=="no" or inicio=="No":
            
            print("listo!!")
            
#Este es el uso de la biblioteca datetime
            
#Con esto podemos agendar la reunion facilmente
            
#con los datos que le pedimos al usuario
            
#con timedelta podemos sumar los dias que faltan

# Finalmente imprimiendo el dia que escogio el usuario
            
            print("La fiesta será el", hoy + ultdia)
            
#Este es el acumulador de cuantas veces se repite el ciclo
            
#Para saber cuantas personas han sido ingresadas
            
            print(acum," personas han sido ingresadas a la reunion")
            
#Este es el acumulador mas grande
            
#ya que contiene los nombres, y la decision de cada uno de los invitados
            
            print(cont)
            
#Se despide
            
            print("Gracias por utilizarme")
            

    
  
