from ddgs import DDGS

def pesquisar_web(pergunta):

    try:

        resultados = DDGS().text(
            pergunta,
            max_results=3
        )

        texto = ""

        for item in resultados:

            texto += f"Título: {item['title']}\n"
            texto += f"Resumo: {item['body']}\n\n"

        return texto

    except Exception as erro:

        return f"Erro: {erro}"