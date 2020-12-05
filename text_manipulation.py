
#Toma la primera letra y el último parámetro menos 1
"""print(my_name[1:3])
print(my_name[0:3])
print(my_name[0:7:2])
print(my_name[::-1])"""

def palindrome(name):
    name=name.lower()
    #Retira los espacios
    name=name.replace(' ','')
    if name[:]==name[::-1]:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

my_name=input('Dime tu nombre ')
palindrome(my_name)