import tkinter as tk

from config import *
from memory import carregar, salvar, registrar_mensagem
from mood import atualizar_humor
from personality import limpar_texto
from prompt_builder import montar_prompt
from brain import gerar_resposta
from internet import pesquisar_web

# ==========================

# CARREGAR MEMÓRIA

# ==========================

memoria = carregar(
MEMORIA_FILE,
{
"usuario": {
"nome": "Gustavo"
},
"humor": "neutro",
"afeto": 70,
"ultimas_mensagens": []
}
)

perfil = carregar(
PERFIL_FILE,
{
"nome_ia": "Capella",
"personalidade_base": "calma, protetora e observadora"
}
)

# ==========================

# JANELA

# ==========================

janela = tk.Tk()
janela.title("Capella V10 Internet")
janela.geometry("600x700")

# ==========================

# CHAT

# ==========================

chat = tk.Text(
janela,
wrap="word",
font=("Consolas", 11)
)

chat.pack(
fill="both",
expand=True,
padx=5,
pady=5
)

# ==========================

# ENTRADA

# ==========================

entrada = tk.Entry(
janela,
font=("Consolas", 12)
)

entrada.pack(
fill="x",
padx=5,
pady=5
)

# ==========================

# FUNÇÃO ENVIAR

# ==========================

def enviar(event=None):


    msg = entrada.get().strip()

    if not msg:
        return

    entrada.delete(0, tk.END)

    chat.insert(
        tk.END,
        f"Você: {msg}\n\n"
    )

    chat.see(tk.END)

    atualizar_humor(
        memoria,
        msg
    )

    registrar_mensagem(
        memoria,
        f"Usuário: {msg}",
        MAX_MEMORIA
    )

    pesquisa = ""

    if msg.lower().startswith("pesquise "):

        termo = msg[9:]

        pesquisa = pesquisar_web(termo)

    prompt = montar_prompt(
        memoria,
        perfil,
        msg
    )

    if pesquisa:

        prompt += f"""
    ```

    Informações encontradas na internet:

    {pesquisa}

    Use essas informações para responder ao usuário.
    """


    print("\n===== PROMPT =====")
    print(prompt)
    print("==================\n")

    try:

        resposta = gerar_resposta(prompt)

        resposta = limpar_texto(resposta)

    except Exception as erro:

        resposta = f"[ERRO] {erro}"

    chat.insert(
        tk.END,
        f"{perfil['nome_ia']}: {resposta}\n\n"
    )

    chat.see(tk.END)

    registrar_mensagem(
        memoria,
        f"Capella: {resposta}",
        MAX_MEMORIA
    )

    salvar(
        MEMORIA_FILE,
        memoria
    )


    # ==========================

    # ENTER

    # ==========================

    entrada.bind(
    "<Return>",
    enviar
)

# ==========================

# BOTÃO

# ==========================

botao = tk.Button(
janela,
text="Enviar",
command=enviar
)

botao.pack(pady=5)

# ==========================

# MENSAGEM INICIAL

# ==========================

chat.insert(
tk.END,
"Capella: Olá. Estou pronta para conversar.\n\n"
)

chat.see(tk.END)

# ==========================

# LOOP

# ==========================

janela.mainloop()
