import requests
from config import MODEL_NAME


def gerar_resposta(prompt):
    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.7
            },
            timeout=120
        )

        if resposta.status_code != 200:
            return f"[ERRO Ollama {resposta.status_code}] {resposta.text}"

        dados = resposta.json()

        if "response" not in dados:
            return f"[ERRO] Resposta sem campo 'response'. Recebi: {dados}"

        texto = dados["response"]

        lixo = [
            "User:",
            "Usuário:",
            "Assistant:",
            "Linlin:",
            "Resposta:",
            "Recent messages:"
        ]

        for item in lixo:
            texto = texto.replace(item, "")

        return texto.strip()

    except requests.exceptions.ConnectionError:
        return "[ERRO] Não consegui conectar no Ollama. Ele está aberto?"

    except requests.exceptions.Timeout:
        return "[ERRO] Ollama demorou demais. Modelo muito pesado?"

    except Exception as erro:
        return f"[ERRO] {type(erro).__name__}: {erro}"
