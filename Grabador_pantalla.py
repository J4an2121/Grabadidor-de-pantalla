import cv2 #OpenCV): Se usa para manipulación de imágenes y videos.
import numpy as np #Se usa para manejar imágenes como matrices de píxeles.
import pyautogui#Permite capturar la pantalla y automatizar interacciones con el mouse/teclado.
import keyboard#Detecta si una tecla específica ha sido presionada.


tamanio_pantalla = pyautogui.size() #Obtiene el tamaño de la pantalla en píxeles 
fps = 15 #Define los fotogramas por segundo 
cv = cv2.VideoWriter_fourcc(*"XVID") #specifica el códec de video XVID, que comprime los datos.
salida = "video.mp4" #Nombre del archivo de video de salida.
video = cv2.VideoWriter(salida, cv, fps, (tamanio_pantalla.width, tamanio_pantalla.height)) #crea el objeto video para escribir los fotogramas en un archivo.

print("Grabando... Presiona 'f' para detener la grabación.")# permite salir bucle y finalizar la grabacion

while True:
    tamanio = pyautogui.screenshot() #Captura la pantalla y la guarda como una imagen
    frame = np.array(tamanio) #Convierte la imagen en un array de NumPy.
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # Convierte la imagen de formato RGB a BGR (necesario para OpenCV).
    video.write(frame) #Agrega el fotograma al video.

    if keyboard.is_pressed('f'): #Verifica si la tecla 'f' ha sido presionada.
        print("Grabación detenida.")
        break

video.release() #ibera los recursos y guarda el video en el archivo.
print(f"Video grabado como:{salida}") #Muestra el nombre del archivo generado.