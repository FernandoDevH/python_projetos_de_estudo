import random
import string

def gerador_senha(tamanho = 8):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    todos_os_caracteres = letras + numeros + simbolos
        
    senha = ""
    # Gera a senha
    for i in range(0, tamanho):
        digitos = random.choice(todos_os_caracteres)
        senha = senha + digitos
        
    return senha

escolha_do_usuario = input("Digite o tamanho da senha desejada: ")

if escolha_do_usuario.isdigit():
    escolha_do_usuario = int(escolha_do_usuario)
else:
    print("Valor inválido. O tamanho da senha deve ser um número inteiro.")
    exit()

senha_gerada = gerador_senha(tamanho = escolha_do_usuario)
print(f"A senha gerada é: {senha_gerada}")
