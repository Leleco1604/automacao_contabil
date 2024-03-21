import openpyxl

workbook = openpyxl.load_workbook("vendas_de_produtos.xlsx")
vendas_sheet = workbook["vendas"]


for linha in vendas_sheet.iter_rows(min_row=2):
    linha[0].value
    linha[1].value
    linha[2].value
    linha[3].value
