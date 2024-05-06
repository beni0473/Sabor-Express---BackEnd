import os

restaurantes = [{"nome":"Sushi", "categoria":"japonesa", "ativo":False}, 
                {"nome":"Pizza Suprema", "categoria":"pizza", "ativo":True},
                {"nome":"Massa da Nona", "categoria":"italiano", "ativo":False}]

def exibir_nome_do_programa():
    print("𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨\n")

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. listar Restaurante")
    print("3. Alternar Restaurante")
    print("4. Sair\n")
    
def finalizar_app():
   exibir_subtitulo("finalizando app")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaunte {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastro com sucesso!\n")
    voltar_menu_principal()
        
def listar_restaurantes():
    exibir_subtitulo("listando restaurantes")

    print(f"{"Nome do Restaurante".ljust(21)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f".{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}") 
    voltar_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" 
            if restaurante["ativo"]:
                print(mensagem) 
            else: print(f"O restaurante {nome_restaurante} foi desativado com sucesso!")

    if restaurante_encontrado == False:
        print("O restaurante não foi encontrado")


    voltar_menu_principal()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()