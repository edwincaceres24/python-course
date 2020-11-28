print("Hola")
print("Cómo te llamas?")
myName=input()
print("Qué tal " + myName + "?")
print("Tu nombre tiene " + str(len(myName)) + " letras")
print('Cuál es tu edad?')
#print(int('99.9')) #Not possible to print
yourAge=int(input())
#yourAge=int(yourAge) #can't evaluate value as an integer, better try yourAge=int(input())
#print(int(1.99)) #Te deja imprimir números flotantes
print("Tienes "+ str(yourAge) +" años " + myName) #cambia a str solo para el print
print("El siguiente año tendrás "+ str(yourAge + 1) + " años")
if yourAge < 4:
    print("Felicidades, eres una Chiquisaurio")
elif myName=="Edwin":
    print("Es usted un agradable sujeto")
elif yourAge> 18:
        print("Eres una Nathisaurio")
