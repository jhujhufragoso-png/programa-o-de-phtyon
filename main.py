def comparar_par_impar(num1, num2):
    # Verifica o primeiro número
    if num1 % 2 == 0:
        res1 = "PAR"
    else:
        res1 = "ÍMPAR"
        
    # Verifica o segundo número
    if num2 % 2 == 0:
        res2 = "PAR"
    else:
        res2 = "ÍMPAR"
        
    print(f"O número {num1} é {res1}.")
    print(f"O número {num2} é {res2}.")

comparar_par_impar(7, 12)









def multiplicar_tres_numeros(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado

# Exemplo de uso:
resultado_final = multiplicar_tres_numeros(2, 3, 4)
print(f"O resultado da multiplicação é: {resultado_final}")








def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado


print(calcular_potencia(2, 3)) 


print(calcular_potencia(5, 2))  








def verificar_idade():
   
    idade = int(input("Digite a sua idade: "))
    
   
    if idade == 18:
        print("Parabéns! Você tem 18 anos e agora alcançou a maioridade.")
    else:
        print(f"Você digitou {idade} anos. Mensagem padrão de acesso.")


verificar_idade()





from datetime import datetime

def calcular_idade(ano_nascimento):
    

    ano_atual = datetime.now().year
    
    
    idade = ano_atual - ano_nascimento
    return idade


ano_nasceu = 2008
resultado = calcular_idade(ano_nasceu)

print(f"Quem nasceu em {ano_nasceu} completa (ou completou) {resultado} anos em {datetime.now().year}.")





def brasil_ganhou_copa(ano):
    
    anos_titulos = {
        1958: "Suécia",
        1962: "Chile",
        1970: "México",
        1994: "Estados Unidos",
        2002: "Coreia do Sul e Japão"
    }
    
    anos_de_copa = [
        1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 
        1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026
    ]
    
    if ano not in anos_de_copa:
        return f"Não teve Copa do Mundo Masculina no ano de {ano}."
    elif ano in anos_titulos:
        return f"Sim! O Brasil ganhou a Copa de {ano} na {anos_titulos[ano]}! 🏆"
    else:
        return f"Houve Copa em {ano}, mas o Brasil não ganhou desta vez. 😢"

resultado = brasil_ganhou_copa(1999)
print(resultado)







def sistema_restaurante():
    
    cardapio = {
        "Salada": 15.00,
        "Macarronada": 28.50,
        "Sanduiche": 18.90,
        "Sorvete": 8.00
    }
    
    # Lista para armazenar o pedido do cliente
    pedido = []
    
    print("--- BEM-VINDO AO NOSSO RESTAURANTE ---")
    
    while True:
        
        print("\n=== CARDÁPIO ===")
        for prato, preco in cardapio.items():
            print(f"- {prato}: R$ {preco:.2f}")
        print("=================")
        
       
        escolha = input("\nDigite o nome do prato que deseja (ou 'sair' para fechar a conta): ").strip().title()
        
       
        if escolha == "Sanduíche": escolha = "Sanduiche"
        
        if escolha.lower() == 'sair':
            break
        elif escolha in cardapio:
            pedido.append(escolha)
            print(f"✔️ {escolha} adicionado ao seu pedido!")
        else:
            print("❌ Opção inválida! Por favor, escolha um item do cardápio.")
         
        
    print("\n--- RESUMO DO PEDIDO ---")
    if not pedido:
        print("Você não escolheu nenhum item. Obrigado pela visita!")
    else:
        total = 0
        for item in pedido:
            print(f"• {item}: R$ {cardapio[item]:.2f}")
            total += cardapio[item]
        
        print("------------------------")
        print(f"VALOR TOTAL: R$ {total:.2f}")
        print("Obrigado pela preferência! Bom apetite!")


sistema_restaurante()