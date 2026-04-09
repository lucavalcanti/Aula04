# #Estrutura If
idade = int(input("Insira a idade: "))

if idade >= 18:
    print ("Você é adulto")
else:
    print('Você não é adulto')

    #--------------------------------------

    pontos = int(input("Informe os pontos: "))
    if pontos >= 100:
        print("Excelente!")
    elif pontos >= 50:
        print("Bom desempenho")
    elif pontos >= 25:
        print("Satisfatório")
    else:
        print("Pratique mais")



        #Operadores AND e OR

        usuario = input("Nome: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso")
        else:
            print("Usuário ou senha incorretos") 


valor_compra = float(input("Insira o valor: "))
if valor_compra >250.00:
    desconto = valor_compra * 0.16
    valor_total = valor_compra - desconto
    print(f"{valor_total}")
else:
    print(f"{valor_compra}")

    usuario = input("Nome: ")
    senha = input("Senha: ")



usuario = input("Nome: ")
senha = input("Senha: ")
 
if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso")
else:
    print("Usuário ou senha incorretos")

#Exemplo ifs encadeados

nota = 2
if nota >=9:
    print("A")
elif nota >=7:
    print("B")
elif nota >=5:
    print("C")
elif nota >=3:
    print("D")
else:
    print("E")




#Exemplo ifs não encadeados

nota = 10
if nota >=9:
    print("A")
if nota >=7:
    print("B")
if nota >=5:
    print("C")
if nota >=3:
    print("D")
else:
    print("E")

#Ifs aninhados
    
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

    