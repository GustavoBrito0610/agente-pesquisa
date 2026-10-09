def limpar_texto(texto):

    texto = texto.replace("!!", ".")
    texto = texto.replace("...", ".")

    return texto.strip()