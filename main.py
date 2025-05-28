#Módulo necesario para hacer los QR
import qrcode

imgagen = qrcode.make("") 

#Aquí debe ir como string el directorio de la imagen, el texto o la URL a hacer QR.

f = open("output.png", "wb") 
imgagen.save(f) 

#Aquí se guarda y bautiza el resultado

f.close() 
#Aquí se cierra el editor
