import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

os.makedirs("documentos", exist_ok=True)

ROTULOS = ["Nome", "CPF", "Cargo", "Data de admissao",
           "Data de desligamento", "Motivo", "Valor liquido"]

docs = [
    ("trct_04.pdf", ["Joao Almeida Prado", "000.000.000-04", "Vendedor",
                     "12/01/2022", "05/10/2026", "Sem justa causa", "R$ 5.210,40"]),
    ("trct_05.pdf", ["Fernanda Lima Duarte", "000.000.000-05", "Assistente Financeiro",
                     "07/07/2019", "18/10/2026", "Pedido de demissao", "R$ 6.780,15"]),
    ("trct_06_incompleto.pdf", ["Ricardo Nunes Barbosa", "", "Motorista",
                     "25/03/2020", "22/10/2026", "Sem justa causa", "R$ 4.095,90"]),
    ("trct_07.pdf", ["Patricia Moura Teixeira", "000.000.000-07", "Recepcionista",
                     "14/11/2023", "28/10/2026", "Acordo entre as partes", "R$ 2.980,00"]),
    ("trct_08.pdf", ["Bruno Castro Azevedo", "000.000.000-08", "Tecnico de Manutencao",
                     "02/09/2021", "30/10/2026", "Pedido de demissao", "R$ 3.845,70"]),
    ("trct_09_incompleto.pdf", ["Luciana Freitas Rocha", "000.000.000-09", "Coordenadora de RH",
                     "19/04/2018", "03/11/2026", "", ""]),
    ("trct_10.pdf", ["Marcos Vinicius Teles", "000.000.000-10", "Auxiliar de Producao",
                     "08/08/2024", "04/11/2026", "Sem justa causa", "R$ 2.455,25"]),
]

for arquivo, valores in docs:
    c = canvas.Canvas(f"documentos/{arquivo}", pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, 790, "TERMO DE RESCISAO DE CONTRATO (FICTICIO)")
    c.setFont("Helvetica", 12)
    y = 740
    for rotulo, valor in zip(ROTULOS, valores):
        if valor:
            c.drawString(60, y, f"{rotulo}: {valor}")
        y -= 28
    c.save()

print("7 documentos novos criados! Total: 10.")