"""import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed' + response + '.')"""

def run (var):
    while var < 1000000:
        print(var)
        var=var*2

your_number=int(input('Your number: '))
run(your_number)