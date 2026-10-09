# 🤖 Linlin — Agente de IA Local

Chatbot de conversação e pesquisa desenvolvido em Python, rodando 100% localmente com [Ollama](https://ollama.com/). A Linlin tem personalidade própria, sistema de memória, humor dinâmico e capacidade de busca na web.

---

## 📌 Sobre o projeto

A Linlin é um assistente de IA **que roda inteiramente no seu computador** — sem depender de APIs pagas, servidores externos ou envio de dados para terceiros.

O projeto foi criado como estudo prático de:
- Integração de LLMs locais com Python
- Arquitetura modular de agentes conversacionais
- Sistemas de memória e personalidade
- Interface gráfica com Tkinter
- Boas práticas de segurança (nunca expor credenciais)

---

## ⚙️ Funcionalidades

- 💬 **Chat interativo** com interface gráfica (Tkinter)
- 🧠 **Memória persistente** — lembra das últimas conversas
- 🎭 **Personalidade configurável** — tom e jeito de falar próprios
- 😊 **Sistema de humor** — reage emocionalmente às mensagens
- 🔍 **Busca na web** — comando `pesquise [termo]` ativa pesquisa no DuckDuckGo
- 🔒 **100% offline** — nenhum dado sai do seu computador

---

## 🛠️ Tecnologias utilizadas

- **Python 3.14**
- **Ollama** — execução local de LLM
- **Gemma 3:4b** — modelo de linguagem do Google
- **Tkinter** — interface gráfica
- **ddgs** — busca na web (DuckDuckGo)
- **JSON** — armazenamento de dados

---

## 🚀 Como executar

### Pré-requisitos

1. [Python 3.10+](https://www.python.org/downloads/) instalado (marque "Add Python to PATH")
2. [Ollama](https://ollama.com/download) instalado
3. Modelo Gemma 3 baixado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/GustavoBrito0610/agente-pesquisa.git
cd agente-pesquisa

# 2. Baixe o modelo no Ollama (uma vez só)
ollama pull gemma3:4b

# 3. Instale as dependências Python
pip install requests ddgs

# 4. Execute
python main.py
