import os
from dotenv import load_dotenv
from interface import ChatbotGUI
from chatbot import Chatbot

# Cargar las variables de entorno
load_dotenv()

# Configurar la API de OpenAI
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("No se ha encontrado la clave de la API de OpenAI en el archivo .env")

# Crear una instancia de la clase `Chatbot`
chatbot = Chatbot(api_key)

# Inicializar la interfaz gráfica
gui = ChatbotGUI(chatbot)
gui.run()
