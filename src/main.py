import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from extrator import ler_pdf, extrair_dados, CAMPOS


def montar_planilha():
    wb = Workbook()
    ws = wb.active
    ws.title = "Documentos"

    ws.append(["arquivo"] + CAMPOS + ["status", "campos_faltando"])
    for celula in ws[1]:
        celula.font = Font(bold=True)

    vermelho = PatternFill("solid", fgColor="FFC7CE")

    for nome in sorted(os.listdir("documentos")):
        if nome.endswith(".pdf"):
            texto = ler_pdf(os.path.join("documentos", nome))
            dados = extrair_dados(texto)

            faltando = [c for c in CAMPOS if not dados.get(c)]
            status = "INCOMPLETO" if faltando else "OK"

            ws.append([nome] + [dados.get(c) for c in CAMPOS]
                      + [status, ", ".join(faltando)])

            if faltando:
                for celula in ws[ws.max_row]:
                    celula.fill = vermelho

    for coluna in ws.columns:
        ws.column_dimensions[coluna[0].column_letter].width = 24

    wb.save("resultado.xlsx")
    print("Planilha criada: resultado.xlsx")


if __name__ == "__main__":
    montar_planilha()