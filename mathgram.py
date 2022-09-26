import random

op = '9+1*(-3)' # put your calc here

op2 = op 
print(eval(op2))
operation = []

for i in op:
    operation.append(i)

lista = []

def bruteforce():
    global lista 
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
                    print(''.join(operation), '=', eval(''.join(operation)))
                    break
                else:
                    print(f'tentei {"".join(operation)} mas deu {ac}, o certo é {eval(op2)}')
        except:
            pass

bruteforce()
