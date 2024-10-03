import openai
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
import json

class Chatbot:
    def __init__(self, api_key, model_name="gpt-3.5-turbo", max_tokens=50, history_file="conversation_history.json"):
        # Configurar la API de OpenAI
        openai.api_key = api_key
        self.history_file = history_file

        # Definir el modelo de lenguaje con el límite de tokens
        self.llm = ChatOpenAI(openai_api_key=api_key, model_name=model_name, max_tokens=max_tokens)

        # Definir la plantilla de prompt para la conversación
        self.prompt = PromptTemplate.from_template("Human: {input}\nAI:")

        # Añadir memoria al chatbot
        self.memory = ConversationBufferWindowMemory(k=5)

        # Crear la cadena de conversación
        self.conversation = self.prompt | self.llm

        # Cargar el historial de conversación
        self.conversation_history = self.load_history()

    def send_message(self, message):
        """Envía un mensaje al chatbot y obtiene una respuesta"""
        # Usar `conversation` para obtener la respuesta
        response = self.conversation.invoke({"input": message})
        self.conversation_history.append({"user": message, "bot": response})
        # Guardar el historial
        self.save_history()
        return response

    def load_history(self):
        """Carga el historial de conversación desde el archivo JSON"""
        try:
            with open(self.history_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_history(self):
        """Guarda el historial de conversación en el archivo JSON"""
        with open(self.history_file, "w") as f:
            json.dump(self.conversation_history, f)
