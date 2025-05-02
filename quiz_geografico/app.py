print("Seja bem vindo ao Quiz!")
score = 0
while True:
    inicio_do_programa = input("Quer começar o quiz? (s/n): ").strip().upper()
    if inicio_do_programa not in ['S', 'N']:
        print("Opção inválida! Por favor, insira 's' para sim ou 'n' para não.")
    elif inicio_do_programa != 'S':
        print("Ok, até a próxima!")
        exit() 
    else:
        print("Você pode responder as perguntas digitando a letra correspondente à resposta correta.\n"
        "Vamos começar!")
        break

print(
    "1. Qual é a capital da França?\n"
    " a) Paris\n"
    " b) Londres\n"
    " c) Berlim\n"
    " d) Madri"
)

while True:
    resposta1 = input("Digite a letra da sua resposta: ").strip().lower()
    if resposta1 not in ['a', 'b', 'c', 'd']:
        print("Opção inválida! Por favor, insira uma das opções (a, b, c ou d).")
    else:
        if resposta1 != 'a':
           print("Incorreto! A resposta correta é a letra a) Paris.")
        else:
            print("Correto!\n")
            score += 1
        break
    


print(
    "2. Qual é a capital da Alemanha?\n"
    " a) Brasilia\n"
    " b) Londres\n"
    " c) Berlim\n"
    " d) Madri"
)
while True:
    resposta2 = input("Digite a letra da sua resposta: ").strip().lower()
    if resposta2 not in ['a', 'b', 'c', 'd']:
        print("Opção inválida! Por favor, insira uma opção válida (a, b, c ou d).\n")
    
    else:
        if resposta2 != 'c':
            print("Incorreto! A resposta correta é a letra c) Berlim.\n")
        else:
            print("Correto!\n")
            score += 1
        break
    
print(f"Sua pontuação final é: {score}/2")
if score == 2:
    print("Parabéns! Você acertou todas as perguntas.")
elif score == 1:
    print("Você acertou uma pergunta.")
else:
    print("Você não acertou nenhuma pergunta.")