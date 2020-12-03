import random

#print random numbers between 1-20
guessnumber = random.randint(1,20)
#Ask to do it six tiemes
print("Guess what is my number")
for guessestime in range(1,7):
    #Se adicionan al for para que se repita la pregunta cada vez
    def mytries():
        tries = 7 - guessestime
        print("That's not my number. You have "+ str(tries) + " more tries")
        #tries=tries-1

    myguess = int(input())
    if guessnumber > myguess:
        print("Your number is lower than mine. Try again")
        mytries()
    elif guessnumber < myguess:
        print("Your number is greater than mine. Try again")
        mytries()
    else:
        break
if myguess==guessnumber:        
    print("Congrats! Your name is equal than mine")
    print("It took you "+ str(guessestime) + " time(s) to figure out that "+ str(guessnumber) + " is my number")
else:
    print("You didn't guess that my number is " + str(guessnumber))

#Cómo contar el número de intentos