import json
import random

f = open("palavras.json", encoding="utf8")
palavras = json.load(f)

escolha_computador = random.choice(list(palavras.keys()))

print(f"Seja bem vindo!! \n"
        "Você tem 5 tentativas para adivinhar a data correta.\n"
        "As datas estão no formato DDMMAAAA.\n")

quantidade_tentativas = 5
win = False

while quantidade_tentativas > 0:
    escolha_usuario = input(f"A dica é: {palavras[escolha_computador]}\n"
                            "Digite seu palpite: ")                       
    
    if len(escolha_usuario) != 8:
        print("Data inválida! Tente novamente.")
        continue
    
    quantidade_tentativas -= 1
    
    print(f"Você ainda tem {quantidade_tentativas} tentativas.")
    
    if escolha_usuario.isdigit():
        pontuacao = 0
        check = []
        for i in range(8):
            if escolha_usuario[i] == escolha_computador[i]:
                check.append("✅")
                pontuacao = pontuacao + 1
                
            else:
                check.append("❌") 
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(escolha_usuario))
        
        print("#####################################################\n")
        
        if pontuacao == 8:
            win = True
            break
            
    else:
        print("Data inválida! Tente novamente.")
        continue
    
if win == True:
    print(f"Parabéns! Você acertou a data correta é: {escolha_computador}")
else:
    print("Você não conseguiu adivinhar a data correta.") 
    print(f"A data correta era: {escolha_computador}")