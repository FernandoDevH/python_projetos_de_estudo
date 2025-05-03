import time

while True:
    valor_inserido = input("Digite o tempo em segundos: ")
    
    if valor_inserido.isdigit():
        valor_inserido = int(valor_inserido)
        
        while valor_inserido >= 0:  
            # Calcular minutos e segundos, o operador divmod retorna o quociente e o resto da divisão
            minuto, segundo = divmod(valor_inserido, 60)
            
            # Formatar o tempo total como mm:ss
            tempo_total = f"{minuto:02d}:{segundo:02d}"
            print(f"Contagem regressiva: {tempo_total}", end="\r")
            time.sleep(1)
            valor_inserido -= 1
        
        print("\nTempo esgotado!")  

        continuar = input("Deseja iniciar outra contagem? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando o programa. Até mais!")
            break

    else:
        print("Valor inválido! O valor deve ser um número inteiro.")
