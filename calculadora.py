#Variables
first_operant=input('Escribe tu primer número ')
second_operant=input('Escribe tu segundo número ')
first_operant=int(first_operant)
second_operant=int(second_operant)
operators = ["Suma", "Resta", "Multiplicar", "Dividir"]
current_operant=""

#Functions
def select_operant(operator):
    print('¿Qué operación deseas realizar?')
    for i in range(0,len(operators),1):
        print(operators[i])
    operator = input("____ ")
    operator = operator.capitalize()
    return operator

def select_current_operant ():
    if current_operant == "Suma":
        print("Tu resultado es: " + str((first_operant + second_operant)))
    elif current_operant =="Resta":
        print("Tu resultado es: " + str((first_operant - second_operant)))
    elif current_operant =="Multiplicar":
        print("Tu resultado es: " + str((first_operant * second_operant)))
    elif current_operant =="Dividir":
        print("Tu resultado es: " + str((first_operant // second_operant)))
    else:
        print("Has colocado un número equivocado")

#Deploy
current_operant=select_operant(current_operant)
print(current_operant)
select_current_operant()
