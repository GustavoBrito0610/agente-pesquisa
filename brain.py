import requests
from config import MODEL_NAME

def gerar_resposta(prompt):

    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.7
        }
    )

    texto = resposta.json()["response"]

    lixo = [
        "User:",
        "Usuário:",
        "Assistant:",
        "Capella:",
        "Resposta:",
        "Recent messages:"
    ]

    for item in lixo:
        texto = texto.replace(item, "")

    return texto.strip()