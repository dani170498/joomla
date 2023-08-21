import subprocess

class DetectarVersionJoomla:
    def ejecutar_nuclei(self, ruta_plantilla, lista_objetivos, directorio_salida):
        try:
            # Construir el comando
            comando = f'nuclei -stats -t "{ruta_plantilla}" -l "{lista_objetivos}" -je "{directorio_salida}/$(basename {ruta_plantilla} .yaml).json"'

            # Ejecutar el comando en la terminal
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

            # Imprimir la salida
            print(resultado.stdout)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    detector = DetectarVersionJoomla()

    ruta_plantilla = "/home/kali/joomla/templatesfuncional"
    lista_objetivos = "/home/kali/joomla/joomla.txt"
    directorio_salida = "/home/kali/joomla/reportes"

    detector.ejecutar_nuclei(ruta_plantilla, lista_objetivos, directorio_salida)


