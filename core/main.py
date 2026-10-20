import sys
from pathlib import Path
from datetime import datetime

# Encontrar la carpeta principal del proyecto JARVIX
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

# Permitir que Python encuentre las carpetas del proyecto
sys.path.insert(0, str(RAIZ_PROYECTO))

from ai.client import preguntar_ia


def mostrar_presentacion():
    print("=" * 45)
    print("       J.A.R.V.I.X - ASISTENTE")
    print("=" * 45)
    print("Sistema iniciado correctamente.")
    print(
        f"Fecha y hora: "
        f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    )
    print("Escribe 'salir' para cerrar el asistente.")
    print("=" * 45)


def iniciar_asistente():
    mostrar_presentacion()

    while True:
        mensaje = input("\nTú: ").strip()

        if not mensaje:
            continue

        if mensaje.lower() == "salir":
            print("JARVIX: Cerrando el sistema. ¡Hasta pronto!")
            break

        print("\nJARVIX está pensando...")

        respuesta = preguntar_ia(mensaje)

        print(f"\nJARVIX: {respuesta}")


if __name__ == "__main__":
    iniciar_asistente()
def iniciar_jarvix():
    print("==============================")
    print("       JARVIX AI SYSTEM")
    print("==============================")

    nombre = input("JARVIX: Hola, ¿cómo te llamas? ").strip()

    print(f"JARVIX: Mucho gusto, {nombre}.")
    print("JARVIX: Escribe 'ayuda' para ver mis comandos.")
    print("JARVIX: Escribe 'salir' para terminar.")

    while True:
        mensaje = input(f"{nombre}: ").strip().lower()

        # Reconocer diferentes saludos
        if mensaje in ["hola", "buenas", "buenos días"]:
            print(f"JARVIX: ¡Hola, {nombre}! ¿En qué puedo ayudarte?")

        # Mostrar los comandos disponibles
        elif mensaje == "ayuda":
            print("JARVIX: Estos son mis comandos:")
            print("- hola: saludar")
            print("- buenas: saludar")
            print("- buenos días: saludar")
            print("- ayuda: mostrar los comandos")
            print("- salir: cerrar JARVIX")

        # Cerrar el programa
        elif mensaje == "salir":
            print(f"JARVIX: Hasta luego, {nombre}.")
            print("JARVIX: Sistema finalizado.")
            break

        # Respuesta para mensajes desconocidos
        else:
            print(
                "JARVIX: Todavía no conozco ese comando. "
                "Escribe 'ayuda' para ver las opciones."
            )


if __name__ == "__main__":
    iniciar_jarvix()
