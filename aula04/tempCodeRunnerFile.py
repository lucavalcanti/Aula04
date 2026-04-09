nota = float(input("Insira a nota: "))
frequencia = float(input("Informe a frequência: "))

if nota >=7:
        #Aprovado por nota, mas precisa chegar a frequência

    if frequencia >=75:
        print("Aluno aprovado por nota e frequência")
    else: 
        print("Reprovado por frequência baixa")
else:
        print("Reprovado por nota baixa:")