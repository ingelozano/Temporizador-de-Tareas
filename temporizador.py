import time
import pygame

def temporizador(segundos):
    pygame.init()
    pygame.mixer.init()

    # Carga el archivo de sonido utilizando una cadena de texto cruda (raw string)
    pygame.mixer.music.load(r"C:\Users\compu\Desktop\Proyectos\Temporizador para Tareas\beep.mp3")

    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + segundos

    while time.time() < tiempo_final:
        tiempo_restante = int(tiempo_final - time.time())
        print(f"Tiempo restante: {tiempo_restante} segundos", end='\r')
        time.sleep(1)

    print("\n¡Tiempo terminado!")

    # Reproduce el sonido cargado
    pygame.mixer.music.play()

    # Espera a que el usuario presione Enter para detener el sonido
    input("Presiona Enter para detener el sonido...")

def main():
    print("Bienvenido al Temporizador de Tareas")
    nombre_tarea = input("Ingresa el nombre de la tarea: ")
    duracion_minutos = int(input("Ingresa la duración en minutos: "))
    
    tiempo_segundos = duracion_minutos * 60
    print(f"Iniciando temporizador para la tarea '{nombre_tarea}'...")
    temporizador(tiempo_segundos)

if __name__ == "__main__":
    main()
