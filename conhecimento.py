import json
import os

ARQUIVO = "conhecimento.json"

def carregar_conhecimento():


    if not os.path.exists(ARQUIVO):

        with open(
            ARQUIVO,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {"conhecimentos": []},
                f,
                ensure_ascii=False,
                indent=4
            )

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


    def salvar_conhecimento(dados):


    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dados,
            f,
            ensure_ascii=False,
            indent=4
        )


    def adicionar_conhecimento(texto):


    dados = carregar_conhecimento()

    if texto not in dados["conhecimentos"]:

        dados["conhecimentos"].append(texto)

        salvar_conhecimento(dados)

