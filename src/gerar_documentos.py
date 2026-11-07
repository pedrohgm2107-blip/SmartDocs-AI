import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

os.makedirs("documentos", exist_ok=True)

campos = [
    ("Nome", "nome"),
    ("CPF", "cpf"),
    ("Cargo", "cargo"),
    ("Data de admissao", "admissao"),
    ("Data de desligamento", "desligamento"),
    ("Motivo", "motivo"),
    ("Valor liquido", "valor"),
]

docs = [
    {"arquivo": "trct_01.pdf", "nome": "Maria Souza Lima", "cpf": "000.000.000-01",
     "cargo": "Auxiliar Administrativo", "admissao": "10/02/2023",
     "desligamento": "15/09/2026", "motivo": "Sem justa causa", "valor": "R$ 4.850,32"},
    {"arquivo": "trct_02.pdf", "nome": "Carlos Pereira Santos", "cpf": "000.000.000-02",
     "cargo": "Operador de Producao", "admissao": "03/05/2021",
     "desligamento": "30/09/2026", "motivo": "Pedido de demissao", "valor": "R$ 3.120,00"},
    {"arquivo": "trct_03_incompleto.pdf", "nome": "Ana Costa Ribeiro", "cpf": "",
     "cargo": "Analista de RH", "admissao": "20/08/2020",
     "desligamento": "10/10/2026", "motivo": "Sem justa causa", "valor": ""},
]

for d in docs:
    c = canvas.Canvas(f"documentos/{d['arquivo']}", pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 790, "TERMO DE RESCISAO DE CONTRATO (FICTICIO)")
    c.setFont("Helvetica", 12)
    y = 740
    for rotulo, chave in campos:
        if d[chave]:
            c.drawString(60, y, f"{rotulo}: {d[chave]}")
        y -= 28
    c.save()

print("Documentos criados na pasta documentos!")
