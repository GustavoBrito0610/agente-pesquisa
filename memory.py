import json

def carregar(caminho, padrao):

    try:

        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    except:

        return padrao


def salvar(caminho, dados):

    with open(caminho, "w", encoding="utf-8") as f:

        json.dump(
            dados,
            f,
            indent=4,
            ensure_ascii=False
        )


def registrar_mensagem(memoria, msg, limite):

    memoria["ultimas_mensagens"].append(msg)

    if len(memoria["ultimas_mensagens"]) > limite:

        memoria["ultimas_mensagens"].pop(0)