import json

def load_history(history_file):
    """Carga el historial de conversación desde el archivo JSON"""
    try:
        with open(history_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_history(history_file, conversation_history):
    """Guarda el historial de conversación en el archivo JSON"""
    with open(history_file, "w") as f:
        json.dump(conversation_history, f)
