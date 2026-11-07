import os
import pdfplumber

pasta = "documentos"

for nome in sorted(os.listdir(pasta)):
    if nome.endswith(".pdf"):
        with pdfplumber.open(os.path.join(pasta, nome)) as pdf:
            texto = ""
            for pagina in pdf.pages:
                texto += (pagina.extract_text() or "") + "\n"
        print("=" * 40)
        print(nome)
        print(texto)