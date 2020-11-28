print('¿Cuántos años tienes carnal?')
yourAge=int(input())
while yourAge<18:
    print("Aún no tienes edad para beber ya que tienes " + str(yourAge) + " años")
    print("Vuelve en " + str(18-yourAge) + " año(s)")
    yourAge= yourAge+1
else:
    print("Ok, puedes meterte unas cervecitas")



while True:
    print('Cómo te llamas?')
    name=input()
    if name != 'Emilia':
        print('Dime tu verdadero nombre por fa')
        #start the Loop
        continue
    print('Hola Emilia. Eres una chiquisaurio. ¿Cuál es tu clave?')
    password = input()
    if password =='Elon':
        print("Buenaaa chola")
        #ends the loop
        break

