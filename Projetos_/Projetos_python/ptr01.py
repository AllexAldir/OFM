from colorama import Fore

# colocando uma biblioteca para cores!
repetir = "sim"
senha = int(9981)
l_nomes = ["Lucas", "João", "Gabriel"]

while repetir == "sim":
    u_nome = input("Digite o nome do usuário: ").capitalize()

    while u_nome not in l_nomes:
        u_nome = input(
            "Nome de usuário não encontrado! Tente novamente: ").capitalize()

    u_senha = int(input("Digite a senha de acesso: "))

    for i in range(0, 3):
        if u_senha == senha:
            break
        else:
            print(f"Senha incorreta tente novamente!")
            u_senha = int(
                input(f"Digite a senha novamente! Restam apenas: {2-i} tentativas: "))

    print("FIM")
    repetir = input("Deseja repetir a operação? 'sim' ou 'não': ").lower()
