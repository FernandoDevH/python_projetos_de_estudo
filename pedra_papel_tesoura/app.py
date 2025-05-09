import random

user_points = 0
computer_points = 0

options = ["Pedra", "Papel", "Tesoura"]

while True:
    user_choice = input("Escolha 0(Pedra), 1(Papel) ou 2(Tesoura) ou 'sair' para encerrar: ").strip()
    
    if user_choice in ["0", "1", "2"]:
        user_choice = int(user_choice)
        computer_choice = random.randint(0, 2)
        computer_option = options[computer_choice]
        
        if user_choice == computer_choice:
            print(f"Empate! Você e o computador escolheram {computer_option}.\n"
                  "Placar atual:\n"
                  f"Você: {user_points} pontos\n"
                  f"Computador: {computer_points} pontos")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            user_points += 1
            print(f"Você venceu! Você escolheu {options[user_choice]} e o computador escolheu {computer_option}.\n"
                  "Placar atual:\n"
                  f"Você: {user_points} pontos\n"
                  f"Computador: {computer_points} pontos")
        else:
            computer_points += 1
            print(f"Computador venceu! Você escolheu {options[user_choice]} e o computador escolheu {computer_option}.\n"
                  "Placar atual:\n"
                  f"Você: {user_points} pontos\n"
                  f"Computador: {computer_points} pontos")
        continue
    elif user_choice == 'sair':
        print(f"Você saiu do jogo. O resultado final é:\n"
              f"Você: {user_points} pontos\n"
              f"Computador: {computer_points} pontos")
       
        if user_points > computer_points:
            print("Você venceu!")
        elif user_points < computer_points:
            print("Computador venceu!")
        else:
            print("Empate!")
        break
    else: 
        print("Opção inválida! Por favor, escolha 0(pedra), 1(papel) ou 2(tesoura).")
        continue
