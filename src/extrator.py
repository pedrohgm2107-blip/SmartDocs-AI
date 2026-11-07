import os
import json
import pdfplumber
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELO = "gemini-3.5-flash-lite"

CAMPOS = ["nome", "cpf", "cargo", "data_admissao",
          "data_desligamento", "motivo", "valor_liquido"]


def ler_pdf(caminho):
    texto = ""
    with pdfplumber.open(caminho) as pdf:
        for pagina in pdf.pages:
            texto += (pagina.extract_text() or "") + "\n"
    return texto


def extrair_dados(texto):
    prompt = f"""Voce extrai dados de termos de rescisao.
Devolva SOMENTE um JSON com estas chaves: {CAMPOS}.
Se um campo nao estiver no documento, use null. Nao invente nada.

Documento:
{texto}"""
    resposta = client.models.generate_content(
        model=MODELO,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        ),
    )
    return json.loads(resposta.text)


if __name__ == "__main__":
    pasta = "documentos"
    for nome in sorted(os.listdir(pasta)):
        if nome.endswith(".pdf"):
            texto = ler_pdf(os.path.join(pasta, nome))
            dados = extrair_dados(texto)
            print("=" * 40)
            print(nome)
            print(json.dumps(dados, ensure_ascii=False, indent=2))