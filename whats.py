import pywhatkit 
 
# Usamos Un try-except
try: 
 
  # Enviamos el mensaje
 
  pywhatkit.sendwhatmsg("+5218991012727",  
                        "Hola soy un robot, Mensaje De Prueba",
                        2,11) 
 
  print("Mensaje Enviado") 
 
  
 
except: 
 
  print("Ocurrio Un Error")