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