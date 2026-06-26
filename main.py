
a = int(input())
b = int(input())

try:
      print(a/b)

except ZeroDivisionError as error:
      print(error)

else:
      print( ' Sem erros')

finally:
      print('Aqui sempre vai printar')


----------------------------------------------------


def trantando_erros():
    try: 
        numero = int(input('>>'))
    except ZeroDivisionError as erro:
        print(erro)
    except ValueError as erro2:
        print('Erro no valor da variável')  
    except NameError as erro:
        print(erro)      
    finally:
        print('O sistema foi carregado')

trantando_erros()


---------------------------------------------------------


def divisao():

    try:
      n1 = float(input('>>'))
      n2 = float(input('>>'))
      div = n1/n2
      print(div)  
    except ZeroDivisionError:
        print("A divisão não ser por zero")
    except ValueError:
        print('Um texo foi digitado')
    except TypeError as erro:
        print(erro)

    else:
        print('Algo deu errado ')    

     
           
divisao() 




import statistics 


def divisao():
    try:
     lista=[0,2,1 , 5]
     moda  =  statistics.mode(lista)
     print(moda)
    except ZeroDivisionError as erro:
        print(erro)
    except TypeError:
        print('Provavelmente digitaram letras')
    except ValueError as erro :
        print(erro)
    except NameError as erro:
        print(erro)    
    except SyntaxError as erro:
        print(erro)     
    finally:
        print('Carregamento finalizado')


divisao()        


  