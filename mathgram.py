import random

op = '9+1*(-3)/(1)'
op2 = op 
print(eval(op2))
operation = []

for i in op:
    operation.append(i)

lista = []
executados = []

def bruteforce():
    global lista 
    global executados 

    for i in range(99999999):
        random.shuffle(operation)
        try:
            if ''.join(operation) not in lista:
                lista.append(''.join(operation))
                try: 
                    ac = eval(lista[-1])
                except:
                    pass

                if ac == eval(op2) and lista[-1] != op:
                    calc = ''.join(operation).replace('+-','-').replace('--','+').replace('(+','(').replace('*+','*')
                    print(calc, '=', eval(calc))
                    break
                else:
                    print(f'tentei {"".join(operation)} mas deu {ac}, o certo é {eval(op2)}')
                    
        except:
            pass

bruteforce()
