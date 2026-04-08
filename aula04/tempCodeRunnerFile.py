valor_compra = float(input("Insira o valor: "))
pagamento = input("Pagamento: ").lower()
if valor_compra >250.00 and pagamento == "vista":
    desconto = valor_compra * 0.16
    valor_total = valor_compra - desconto
    print(f"{valor_total}")
else:
    print(f"{valor_compra}")