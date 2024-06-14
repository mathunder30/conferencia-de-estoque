arroz = 0
feijao = 0
macarrao = 0
leite = 0
ovo = 0
Produtos_Estoque = 100
for x in range(Produtos_Estoque):
    print("Escolha uma das opções: ")
    print("1. Acrescentar produto. ")
    print("2. Tirar produto. ")
    print("3. Verificar Estoque. ")
    print("4. Sair")
    opcao = int(input())

    if opcao == 1:
        produto = int(input("Escolha a opção que você deseja acrescentar: 1. Arroz, 2. Feijão, 3. Macarrão, 4. Leite, 5. Ovos "))
        if produto == 1:
            print("adicionar Arroz")
            adicionar = int(input("quantos que voce quer adicionar? "))
            print (f"Você adicionou {adicionar} arroz")
            arroz += adicionar
        elif produto == 2:
            print("adicionar Feijão")
            adicionar = int(input("quantos que voce quer adicionar? "))
            print (f"Você adicionou {adicionar} Feijão")
            feijao += adicionar
        elif produto == 3:
            print("adicionar Macarrão")
            adicionar = int(input("quantos que voce quer adicionar? "))
            print (f"Você adicionou {adicionar} Macarrão")
            macarrao += adicionar
        elif produto == 4:
            print("adicionar Leite")
            adicionar = int(input("quantos que voce quer adicionar? "))
            print (f"Você adicionou {adicionar} Leite")
            leite += adicionar
        elif produto == 5:
            print("adicionar Ovos")
            adicionar = int(input("quantos que voce quer adicionar? "))
            print (f"Você adicionou {adicionar} Ovos")
            ovo += adicionar



    if opcao == 2:
        print("Escolha a opção que você deseja subtrair: ") 
        print("1. Arroz")
        print("2. Feijão")
        print("3. Macarrão")
        print("4. Leite")
        print("5. Ovos")
        produto = int(input())
        if produto == 1:
            print("subtrair Arroz ")
            adicionar = int(input("quantos que voce quer subtrair "))
            print (f"Você removeu {adicionar} arroz")
            arroz -= adicionar
        elif produto == 2:
            print("subtrair Feijão! ")
            adicionar = int(input("quantos que voce quer subtrair? "))
            print (f"Você Removeu {adicionar} Feijão")
            feijao -= adicionar
        elif produto == 3:
            print("subtrair Macarrão")
            adicionar = int(input("quantos que voce quer subtrair? "))
            print (f"Você Removeu {adicionar} Macarrão")
            macarrao -= adicionar
        elif produto == 4:
            print("subtrair Leite")
            adicionar = int(input("quantos que voce quer subtrair? "))
            print (f"Você Removeu {adicionar} Leite")
            leite -= adicionar
        elif produto == 5:
            print("subtrair Ovos")
            adicionar = int(input("quantos que voce quer subtrair? "))
            print (f"Você Removeu {adicionar} Ovos")
            ovo -= adicionar
    elif opcao == 3:
        print("Digite o numero do produto que você quer verificar: ")
        print("1. Arroz")
        print("2. Feijão")
        print("3. Macarrão")
        print("4. Leite")
        print("5. Ovos")
        produto = int(input())
        if produto == 1:
            print("Arroz: ", arroz)
        elif produto == 2:
            print("Feijão: ", feijao)
        elif produto == 3:
            print("Macarrão: ", macarrao)
        elif produto == 4:
            print("Leite: ", leite)
        elif produto == 5:
            print("Ovos: ", ovo)
    elif opcao == 4:
        print("Saindo...")
        break
    
        





