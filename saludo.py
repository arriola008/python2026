from pathlib import Path
class Saludo:
#Clase constructor no es obligatorio pero recomendable si no hace nada.
    def __init__(self):
        pass

    def saludar(self):
        print("Hola mundo")

        if __name__ == "__main__":
            misaludo = Saludo()
            print(f"Hola Mundo desde {Path(__file__).name}que esta en la ruta {Path(__file__).parent}")
            print(f"Nombre del archivo: {Path(__file__).stem}")
            print(f"Extensión del archivo: {Path(__file__).suffix}")
            misaludo.hola()

            #comentario de prueba