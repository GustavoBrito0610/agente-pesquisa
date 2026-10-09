import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

ARQUIVO_CHAVE = "capellaaiv10-firebase-adminsdk-fbsvc-ca8d44dee0.json"

if not firebase_admin._apps:

    cred = credentials.Certificate(
        ARQUIVO_CHAVE
    )

    firebase_admin.initialize_app(
        cred
    )

db = firestore.client()


def salvar_memoria(texto):

    db.collection(
        "memorias"
    ).add(
        {
            "texto": texto
        }
    )


def salvar_conhecimento(titulo, conteudo):

    db.collection(
        "conhecimentos"
    ).add(
        {
            "titulo": titulo,
            "conteudo": conteudo
        }
    )


def salvar_inferencia(conclusao):

    db.collection(
        "inferencias"
    ).add(
        {
            "conclusao": conclusao
        }
    )

