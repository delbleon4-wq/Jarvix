
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
