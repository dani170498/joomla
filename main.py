from src.detectVersionJoomla import DetectarVersionJoomla
from sys import *
detectorJoomlaVersion = DetectarVersionJoomla()
def menu():

	print ('menu de opciones, escoge una:')
	print ('1. detectar version de joomla')
	print ('2. detectar versiones de plugins')
	print ('3. detectar vulnerabilidades de CVEs')
if __name__ == "__main__":
	while True:
		menu()
		opcion = input("Seleccione una opción: ")
		if opcion == "1":
			detectorJoomlaVersion.ejecutar_nuclei('ruta_plantilla', 'lista_objetivos', 'directorio_salida')
			print ('se ejecuto el script')
		elif opcion == "2":
			print ('resultado2')
		elif opcion == "3":
			print("resultado3")
		else:
			print("Opción no válida. Por favor, seleccione una opción válida.")

