
#Función para mostrar la moneda y el tc dináminco
def conversor (available_currency,tc_exachange):
    print('Hola, ¿cuántos ' + available_currency + ' vas a cambiar?')
    my_currency=float(input()) 
    print('De acuerdo, recibirás '+ str(round(my_currency/tc_exachange,2))+ ' dólares')

available_currency = ["PEN","CHI","MEX","ARG"]


print('Hola, ¿Cuál es tu nombre?')
customer_name=input()
print('Hola ' + customer_name.capitalize() +', ¿qué moneda vas a cambiar? Elige una opción')
for exchanges in available_currency:
    print("- " + exchanges)
my_currency=input()    

if my_currency == "PEN":
    conversor("soles",3.65)
elif my_currency =="CHI":
    conversor("pesos chilenos",3875)
elif my_currency =="MEX":
    conversor("pesos mexicanos", 2560)
elif my_currency =="ARG":
    conversor("pesos argentinos",97)
else:
    print('Lo siento, no ofrecemos cambio para esa moneda')



#Este comentario lo hice en la rama Master
#print Estos cambios los hice en la rama cambios
#Este comentario se subirá usando un protocolo de seguridad SSH
#Este comentario debe hacerse con el archivo
