import os
from datetime import datetime
import uuid

# lista de feedbacks
feedbacks = []
lista_planos_de_carreira = []

def tecla_voltar_menu():
    print("\nPressione qualquer tecla para voltar ao menu...")
    input()  # pausa o programa até que o usuário pressione alguma tecla
    main()


def exibir_nome_do_programa():
    print(
        """
███╗░░░███╗███████╗██╗░░░██╗░██████╗  ███████╗███████╗███████╗██████╗░██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗
████╗░████║██╔════╝██║░░░██║██╔════╝  ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝
██╔████╔██║█████╗░░██║░░░██║╚█████╗░  █████╗░░█████╗░░█████╗░░██║░░██║██████╦╝███████║██║░░╚═╝█████═╝░╚█████╗░
██║╚██╔╝██║██╔══╝░░██║░░░██║░╚═══██╗  ██╔══╝░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██╔══██║██║░░██╗██╔═██╗░░╚═══██╗
██║░╚═╝░██║███████╗╚██████╔╝██████╔╝  ██║░░░░░███████╗███████╗██████╔╝██████╦╝██║░░██║╚█████╔╝██║░╚██╗██████╔╝
╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░\n"""
    )


def exibir_menu():
    print("1. Cadastrar feedback")
    print("2. Listar feedbacks")
    print("3. Deletar feedback")
    print("4. Detalhes do feedback")
    print("5. Cadastro ou atualização do plano de carreira")
    print("6. Plano de carreira")
    print("7. Sair\n")


def finalizar_app():
    os.system(
        "cls"
    )  # biblioteca para limpar a tela do terminal ao finalizar o aplicativo - vai limpar e em seguida mostra a msg abaixo usando o cls clear screen
    print("""
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░░░██░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░█░░░░░░██░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n""")


def cadastrar_feedback():
    os.system("cls")
    id_feedback = str(
        uuid.uuid4()
    )  # gera um ID único para cada feedback usando a biblioteca uuid
    nome_analista = input("Digite o nome do analista: ")
    data = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )  # pega a data e hora atual e formata para o formato desejado
    motivo = input(
        "Digite o motivo do feedback (Situação, ocorrência ou acompanhamento de rotina): \n"
    )
    pontos_positivos = input(f"Digite os pontos positivos do/da {nome_analista}: \n")
    pontos_de_melhorias = input(f"Digite os pontos de melhorias do/da {nome_analista}: \n")
    plano_de_acao = input(f"Digite o plano de ação para o/a {nome_analista}: \n")
    observações = input("Digite observações adicionais (opcional): \n")
    feedbacks.append(
        (id_feedback, nome_analista, data, motivo, pontos_positivos, pontos_de_melhorias, plano_de_acao, observações)
    )  # adiciona os detalhes do feedback à lista de detalhes do feedback essa lista será utilizada pra trazer os detalhes)
    print("\n" + "=" * 50)
    print("📋 REGISTRO DE FEEDBACK")
    print("=" * 50)  # coloco 50 - traçejados para separar as seções do feedback
    print(f"🆔 ID: {id_feedback}")
    print(f"👤 Analista: {nome_analista}")
    print(f"🕒 Data: {data}")
    print("-" * 50)
    print(f"📌 Motivo:\n{motivo}")
    print("-" * 50)
    print(f"✅ Pontos Positivos:\n{pontos_positivos}")
    print("-" * 50)
    print(f"⚠️ Pontos de Melhoria:\n{pontos_de_melhorias}")
    print("-" * 50)
    print(f"🛠 Plano de Ação:\n{plano_de_acao}")
    print("-" * 50)
    print(f"📝 Observações:\n{observações}")
    print("=" * 50)
    print("\nFeedback cadastrado com sucesso!")
    tecla_voltar_menu()


def listar_feedbacks():
    os.system("cls")
    print("Lista de feedbacks registrados:\n")

    if not feedbacks:  # verifica se a lista está vazia
        print("Nenhum feedback registrado.\n")
        tecla_voltar_menu()
        return

    for feedback in feedbacks:  # percorre a lista
        print(f"ID: {feedback[0]} | Analista: {feedback[1]} | Data: {feedback[2]}")

    tecla_voltar_menu()


def detalhes_feedback():
    os.system("cls")
    
    # percorre a lista de feedbacks para encontrar o feedback com o ID correspondente e lista de acordo com cada campo do feedback
    if not feedbacks:  # verifica se a lista está vazia
          print("Nenhum feedback registrado.\n")
          tecla_voltar_menu()
          return
    id_feedback = input("Digite o ID do feedback para ver os detalhes: ")   
    for (feedback) in (feedbacks):            
        if feedback[0] == id_feedback: #imprime os detalhes do feedback encontrado com o ID correspondente
            print("\n" + "=" * 60)
            print("📋 DETALHES DO FEEDBACK")
            print("=" * 60)

            print(f"🆔 ID: {id_feedback}")
            print(f"👤 Analista: {feedback[1]}")
            print(f"🕒 Data: {feedback[2]}")

            print("-" * 60)
            print("📌 Motivo:")
            print(feedback[3])

            print("-" * 60)
            print("✅ Pontos Positivos:")
            print(feedback[4])

            print("-" * 60)
            print("⚠️ Pontos de Melhoria:")
            print(feedback[5])

            print("-" * 60)
            print("🛠 Plano de Ação:")
            print(feedback[6])

            print("-" * 60)
            print("📝 Observações:")
            print(feedback[7])

            print("=" * 60)
            tecla_voltar_menu()
            return
    else:
        print("Feedback não encontrado. Por favor, verifique o ID e tente novamente.")
        tecla_voltar_menu()

def input_detalhes_plano_de_carreira():
    os.system("cls")
    tipo_analista = input("É um novo analista ou um analista já cadastrado? (Digite 'novo' ou 'cadastrado'): ").lower()
    if tipo_analista == 'novo':
      print("\nCadastro de plano de carreira para novo analista.\n")
      nome_analista = input("Digite o nome do analista para cadastrar o plano de carreira: ")
      cargo_atual = input("Digite o cargo atual do analista: ")
      cargo_desejado = input("Digite o cargo desejado pelo analista: ")
      habilidades_necessarias = input("Digite as habilidades necessárias para alcançar o cargo desejado: ")
      observação = input("Digite alguma observação sobre o plano de carreira: ")
      lista_planos_de_carreira.append((nome_analista, cargo_atual, cargo_desejado, habilidades_necessarias, observação))  # adiciona os detalhes do plano de carreira à lista de plano de carreira
      print("\nPlano de carreira cadastrado com sucesso!")
    else:
        nome_analista = input("Digite o nome do analista cadastrado: ")
        for i, plano in enumerate(lista_planos_de_carreira):  # percorre a lista de plano de carreira para encontrar o plano com o nome do analista correspondente e lista de acordo com cada campo do plano de carreira
            if plano[0] == nome_analista:
                print("\n" + "=" * 60)
                print("📋 DETALHES DO PLANO DE CARREIRA")
                print("=" * 60)

                print(f"👤 Analista: {plano[0]}")
                print(f"📌 Cargo Atual: {plano[1]}")
                print(f"📌 Cargo Desejado: {plano[2]}")
                print(f"📌 Habilidades Necessárias: {plano[3]}")
                print(f"📌 Observação: {plano[4]}")

                print("=" * 60)
                
                nova_observacao = input("\nDeseja adicionar uma nova observação? (s/n): ")
                if nova_observacao.lower() == 's':
                    observacao_adicional = input("Digite a nova observação: ")
                    # Atualiza a lista com a nova observação
                    lista_planos_de_carreira[i] = (plano[0], plano[1], plano[2], plano[3], plano[4] + " | " + observacao_adicional)
                    print("Nova observação adicionada com sucesso!")
                break
        else:
            print("Analista não encontrado. Por favor, cadastre o plano de carreira para este analista primeiro.")   
    tecla_voltar_menu()
     
def plano_de_carreira():
    os.system("cls")
    print("Lista de analistas:")
    for plano in lista_planos_de_carreira:
      print(plano[0])
    analista_escolhido = input("Qual analista você deseja visualizar o plano de carreira? ")  # le e converte pra inteiro a opção do analista escolhido
    for plano in lista_planos_de_carreira:  # percorre a lista de plano de carreira para encontrar o plano com o nome do analista correspondente e lista de acordo com cada campo do plano de carreira
          if plano[0].lower() == analista_escolhido.lower():
                print("\n" + "=" * 60)
                print("📋 DETALHES DO PLANO DE CARREIRA")
                print("=" * 60)

                print(f"👤 Analista: {plano[0]}")
                print(f"📌 Cargo Atual: {plano[1]}")
                print(f"📌 Cargo Desejado: {plano[2]}")
                print(f"📌 Habilidades Necessárias: {plano[3]}")
                print(f"📌 Observação: {plano[4]}")

                print("=" * 60)
                
                break
    else:
        print("Analista não encontrado. Por favor, cadastre o plano de carreira para este analista primeiro.")
    tecla_voltar_menu()

def deletar_feedback():
    id_feedback = input("\nDigite o ID do feedback que deseja deletar: ")
    if id_feedback:
        for i, feedback in enumerate(feedbacks):
            if feedback[0] == id_feedback:
                del feedbacks[i]
                print("Feedback deletado com sucesso!")
                tecla_voltar_menu()
                break                
        else:
            print("Feedback não encontrado. Por favor, verifique o ID e tente novamente.")
            tecla_voltar_menu()
  
def opcao_invalida():
    print("\nOpção inválida.")
    tecla_voltar_menu()


def escolher_opções():
    try:
        opcao_escolhida = int(
            input("Escolha uma opção: ")
        )  # lê a opção escolhida pelo usuário e converte para inteiro
        if opcao_escolhida == 1:
            cadastrar_feedback()
        elif opcao_escolhida == 2:
            listar_feedbacks()
        elif opcao_escolhida == 3:
            deletar_feedback()
        elif opcao_escolhida == 4:  
            detalhes_feedback()
        elif opcao_escolhida == 5:
          input_detalhes_plano_de_carreira()
        elif opcao_escolhida == 6:
            plano_de_carreira()            
        elif opcao_escolhida == 7:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:  # exceção para valor não INT
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opções()


if __name__ == "__main__":
    main()
