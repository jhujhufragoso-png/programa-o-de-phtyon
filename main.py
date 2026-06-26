def valor_hora(carga, salario):
    return salario / carga

def extra_50(valor_hora):
    return valor_hora * 1.5

def salario_total(quantidade_extra, salario, extra_50_):
    valor_q = quantidade_extra * extra_50_
    total   =  valor_q + salario
    return total, valor_q


def sistema_RH():
    carga  = float(input('Carga: '))
    salario = float(input('Salário: '))
    v_h  = valor_hora(carga, salario)
    print(f'Valor hora: , {v_h:.2f}')
    print('------------- ')
    print('HORA EXTRA 50% ')
    ex_50 = extra_50(v_h)
    print(f'{ex_50:.2f}')
    print('------------- ')
    quantidade = float(input('Extra quantidade: '))
    sal = salario_total(quantidade, salario, ex_50 )
    print('R$', round(sal[0],2), "Total hora extra",  round(sal[1],2))
sistema_RH()