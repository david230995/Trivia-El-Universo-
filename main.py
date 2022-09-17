import random
import time

#rcs = random.randint(0, 10)
iniciar_trivia = True
intentos = 0
rcs = 0
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(BLUE +"----- Bienvenid@ a la Trivia del Universo -----"+RESET)
print()
print (BLUE+"Pondremos a prueba tus conocimientos sobre el universo.La trivia constara de 5 preguntas"+RESET)
nombre = input(CYAN+"Por favor ingresa tu nombre:"+RESET)
print()
print(BLUE+"Hola "+RESET, nombre, BLUE+" bienvenido, recuerda ingresar la letra de tu respuesta en minuscula"+RESET)
print()
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  rcs = 0
  print (MAGENTA+"Comenzaras con: ", rcs, " puntos, recuerda que por cada respuesta correcta ganaras 1 punto"+RESET)
  print()
  print()

  
  print(BLUE+"\nIntento número:"+RESET, intentos)
  input(BLUE+"Presiona Enter para continuar"+RESET)
  #for numero_carga in range(5, 0, -1):
  #print(numero_carga)
  #time.sleep(1)
  print()
  print(MAGENTA+"1.¿Cuál es la estrella más cercana al sistema solar?"+RESET)
  print()
  print(CYAN+"a) VY Canis Majoris"+RESET)
  print(CYAN+"b) Eta Carinae"+RESET)
  print(CYAN+"c) Proxima Centauri"+RESET)
  print(CYAN+"d) Betelgeuse"+RESET)
  print()
  ru = input(BLUE+"Escribe la letra correcta en minuscula: "+RESET)
  print()
  
  while ru not in ("a", "b", "c", "d"):
    ru = input(RED+"Debes responder a, b, c o d . Ingresa nuevamente tu respuesta: "+RESET)
  #rc = "a"
  if ru == "a":
    #rcs = rcs /2
    print(RED+"Totalmente incorrecto!", nombre," "+RESET)
  elif ru == "b":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, +" "+RESET)
  #elif ru == "x":
    #rcs = rcs * 2
    #print(GREEN+"Este es un mensaje secreto:Felicidades ",nombre," tu puntaje se multiplico x 2"+RESET)
  elif ru == "d":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)  
  else:
    rcs =rcs + 1
    print(GREEN+"Muy bien", nombre, " ganaste 1 punto"+RESET)
  print()
  print()
  print(BLUE+nombre, "llevas", rcs, "puntos"+RESET)
  print()
  print()
  time.sleep(2) # Espera 2 segundos antes de continuar.
  
  print()
  print(MAGENTA+"2.Más allá de la órbita de Neptuno, existe un conjunto de más de 800 objetos que al igual que el resto de planetas gira alrededor del Sol ¿sabes como identifican los astrónomos a este conjunto de rocas espaciales del que estamos hablando?"+RESET)
  print()
  print(CYAN+"a) Cinturón de Santy"+RESET)
  print(CYAN+"b) Cinturón de Orión"+RESET)
  print(CYAN+"c) Cinturón de Kuiper"+RESET)
  print(CYAN+"d) Cinturón de Triton"+RESET)
  print()
  ru = input(BLUE+"Escribe la letra correcta en minuscula: "+RESET)
  print()
  
  while ru not in ("a", "b", "c", "d"):
    ru = input(RED+"Debes responder a, b, c o d . Ingresa nuevamente tu respuesta: "+RESET)
  #rc = "a"
  if ru == "a":
    #rcs = rcs /2
    print(RED+"Totalmente incorrecto!", nombre," "+RESET)
  elif ru == "b":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)
 # elif ru == "x":
   # rcs = rcs * 2
    #print(GREEN+"Este es un mensaje secreto:Felicidades ",nombre," tu puntaje se multiplico x 2"+RESET)
  elif ru == "d":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)  
  else:
    rcs =rcs + 1
    print(GREEN+"Muy bien", nombre, " ganaste 1 punto"+RESET)
  print()
  print()
  print(BLUE+nombre, "llevas", rcs, "puntos"+RESET)
  print()
  print()
  time.sleep(2) # Espera 2 segundos antes de continuar.
  
  print()
  print(MAGENTA+"3.¿Sabes hace cuánto se formó el sistema solar?"+RESET)
  print()
  print(CYAN+"a) Hace aproximadamente 4.500 millones de años"+RESET)
  print(CYAN+"b) Hace aproximadamente unos 450.000 millones de años"+RESET)
  print(CYAN+"c) Hace aproximadamente unos 450 millones de años"+RESET)
  print(CYAN+"d) Hace aproximadamente unos 45 millones de años"+RESET)
  print()
  ru = input(BLUE+"Escribe la letra correcta en minuscula: "+RESET)
  print()
  
  while ru not in ("a", "b", "c", "d"):
    ru = input(RED+"Debes responder a, b, c o d . Ingresa nuevamente tu respuesta: "+RESET)
  #rc = "a"
  if ru == "b":
    #rcs = rcs /2
    print(RED+"Totalmente incorrecto!", nombre," "+RESET)
  elif ru == "c":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)
  #elif ru == "x":
    #rcs = rcs * 2
    #print(GREEN+"Este es un mensaje secreto:Felicidades ",nombre," tu puntaje se multiplico x 2"+RESET)
  elif ru == "d":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)  
  else:
    rcs =rcs + 1
    print(GREEN+"Muy bien", nombre, " ganaste 1 punto"+RESET)
  print()
  print()
  print(BLUE+nombre, "llevas", rcs, "puntos"+RESET)
  print()
  print()
  time.sleep(2) # Espera 2 segundos antes de continuar.
  print()

  
  print(MAGENTA+"4.¿Cuál es la edad del Universo?"+RESET)
  print()
  print(CYAN+"a) 19.787 millones de años"+RESET)
  print(CYAN+"b) 13.787 millones de años"+RESET)
  print(CYAN+"c) 15.787 millones de años"+RESET)
  print(CYAN+"d) 20.787 millones de años"+RESET)
  print()
  ru = input(BLUE+"Escribe la letra correcta en minuscula: "+RESET)
  print()
  
  while ru not in ("a", "b", "c", "d"):
    ru = input(RED+"Debes responder a, b, c o d . Ingresa nuevamente tu respuesta: "+RESET)
  #rc = "a"
  if ru == "a":
    #rcs = rcs /2
    print(RED+"Totalmente incorrecto!", nombre," "+RESET)
  elif ru == "c":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)
  #elif ru == "x":
    #rcs = rcs * 2
    #print(GREEN+"Este es un mensaje secreto:Felicidades ",nombre," tu puntaje se multiplico x 2"+RESET)
  elif ru == "d":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)  
  else:
    rcs =rcs + 1
    print(GREEN+"Muy bien", nombre, " ganaste 1 punto"+RESET)
  print()
  print()
  print(BLUE+nombre, "llevas", rcs, "puntos"+RESET)
  print()
  print()
  time.sleep(2) # Espera 2 segundos antes de continuar.
  print()

  
  print()
  print(MAGENTA+"5.¿Cual es la mayor estructura conocida en el Universo?"+RESET)
  print()
  print(CYAN+"a) La nebulosa de la tarántula"+RESET)
  print(CYAN+"b) El Agujero negro mas grande: TON 618"+RESET)
  print(CYAN+"c) La Galaxia más grande: IC 1101"+RESET)
  print(CYAN+"d) La Gran Muralla Hércules Corona Boreal"+RESET)
  print()
  ru = input(BLUE+"Escribe la letra correcta en minuscula: "+RESET)
  print()
  
  while ru not in ("a", "b", "c", "d"):
    ru = input(RED+"Debes responder a, b, c o d . Ingresa nuevamente tu respuesta: "+RESET)
  #rc = "a"
  if ru == "a":
    #rcs = rcs /2
    print(RED+"Totalmente incorrecto!", nombre," "+RESET)
  elif ru == "b":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)
  #elif ru == "x":
    #rcs = rcs * 2
    #print(GREEN+"Este es un mensaje secreto:Felicidades ",nombre," tu puntaje se multiplico x 2"+RESET)
  elif ru == "c":
    #rcs = rcs - 5
    print(RED+"Incorrecto!", nombre, " "+RESET)  
  else:
    rcs =rcs + 1
    print(GREEN+"Muy bien", nombre, " ganaste 1 punto"+RESET)
  print()
  print()
  print(BLUE+nombre, "llevas", rcs, "puntos"+RESET)
  print()
  print()
  time.sleep(2) # Espera 2 segundos antes de continuar.
  print()
  
  print(CYAN+"--- Resultados ---"+RESET)
  
  print()
  print(GREEN+"Numero de respuestas correctas:"+RESET)
  print(GREEN+"",rcs,""+RESET)
  print(RED+"Numero de respuestas incorrectas:"+RED) 
  print (RED+"",5 - rcs,""+RESET) 
  print()
  print(CYAN+"Total de respuestas: 5"+RESET)
  
  repetir_trivia = True                          
  
  while repetir_trivia:                          
    print(CYAN+"Trivia"+RESET)                          
    print(CYAN+"opción: si ó no..."+RESET)                           
    respuesta = input(CYAN+"¡Deseas jugar de nuevo?: "+RESET) 
  
    if respuesta == "si":                           
        print(CYAN+"¡Genial!por favor, Corre nuevamente el programa"+RESET) 
        repetir_trivia = False 
    else:                                                
        if respuesta == "si":         
           print(CYAN+"¡Genial!por favor, Corre nuevamente el programa"+RESET)   
           repetir_trivia = False
           while respuesta != "si" and respuesta !="no":                                             
              print(CYAN+"No te entendí")                                           
              respuesta = input(CYAN+"¿Deseas jugar de nuevo?: "+RESET)                    
        if respuesta == "no":                                         
            print(CYAN+"Gracias por participar"+RESET)           
            repetir_trivia = False                            
        else:                                                            
              print("----------------") 