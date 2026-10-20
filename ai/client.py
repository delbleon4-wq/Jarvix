
import os

from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables privadas desde el archivo .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key) if api_key else None


def preguntar_ia(mensaje: str) -> str:
    """Envía un mensaje a la IA y devuelve su respuesta."""

    if client is None:
        return (
            "Todavía no tengo una clave API configurada. "
            "Configura OPENAI_API_KEY en el archivo .env."
        )

    try:
        respuesta = client.responses.create(
            model="gpt-4.1-mini",
            input=mensaje,
        )

        return respuesta.output_text

    except Exception as error:
        print(f"Error al comunicarse con la IA: {error}")
        return "No pude obtener una respuesta. Revisa la conexión y la configuración."
