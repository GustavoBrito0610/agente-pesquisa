import os

PASTA_MODULOS = "modules"


def criar_modulo(nome, codigo):

    os.makedirs(
        PASTA_MODULOS,
        exist_ok=True
    )

    arquivo = os.path.join(
        PASTA_MODULOS,
        f"{nome}.py"
    )

    with open(
        arquivo,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(codigo)

    return arquivo