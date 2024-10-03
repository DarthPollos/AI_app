import tkinter as tk

class ChatbotGUI:
    def __init__(self, chatbot):
        """Inicializa la interfaz gráfica con el chatbot"""
        self.chatbot = chatbot

        # Configuración de la interfaz gráfica
        self.root = tk.Tk()
        self.root.title("Chatbot")

        # Opción para eliminar la advertencia de Secure Coding en macOS (opcional)
        self.root.applicationSupportsSecureRestorableState = lambda: True

        self.chat_log = tk.Text(self.root)
        self.chat_log.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        send_button = tk.Button(self.root, text="Enviar", command=self.send_message)
        send_button.pack()

    def send_message(self):
        """Función para enviar mensajes y mostrar la respuesta"""
        pregunta = self.entry.get()
        if pregunta:
            # Obtener respuesta del chatbot
            respuesta = self.chatbot.send_message(pregunta)

            # Mostrar el mensaje y la respuesta en el chat
            self.chat_log.insert(tk.END, f"Tú: {pregunta}\nChatbot: {respuesta}\n")
            self.entry.delete(0, tk.END)

    def run(self):
        """Ejecuta el bucle principal de la interfaz gráfica"""
        self.root.mainloop()
