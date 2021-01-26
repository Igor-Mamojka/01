data = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

oddelovac = '-' * 35
print(oddelovac)
print('Welcome to the app. Please log in.')
print(oddelovac)

username = str(input('USERNAME: '))
password = str(input('PASSWORD: '))

if data.get(username) == password:
    print('You can continue.')
elif data.get(username) != password:
    print('Password or username is wrong.')

TEXTS = ['''That rises sharply some 1000 feet above 
Twin Creek Valley to an elevation of more 
than 7500 feet above sea level. The butte 
is located just north of US 30 N ''',

'''Python was created in the late 1980 s, and first
released in 1991, by Guido van Rossum as a successor
to the ABC programming language. Python 2.0, 
released in 2000, introduced new features... ''',

'''The United States of America (USA), commonly
known as the United States is a country primarily
located in North America, consisting of 50 states,
a federal district, 5 major self-governing territories... ''']

print(oddelovac)
print('We have 3 texts to be analyzed.')

input = int(input('Enter a number btw. 1 and 3 to select: '))
print(oddelovac)
text = TEXTS[input-1]
slova = []
for slovo in text.split():
    slovo = slovo.strip('\.,:/;')
    slova.append(slovo)

titlecase = 0
lowercase = 0
uppercase = 0
numeric   = 0
pocet     = {}
all_numb  = 0

x = 0
while x < len(slova):
    if slova[x].istitle():
        titlecase = titlecase + 1
    elif slova[x].isupper():
        uppercase = uppercase + 1
    elif slova[x].islower():
        lowercase = lowercase + 1
    elif slova[x].isnumeric():
        numeric = numeric + 1
        all_numb = all_numb + float(slova[x])

    l = len(slova[x])
    pocet[l] = pocet.get(l, 0) + 1
    x = x + 1
print(oddelovac)
print(f'There are {len(slova)} words in the text.')
print(f'There are {titlecase:>2} titlecase words.')
print(f'There are {uppercase:>2} uppercase words.')
print(f'There are {lowercase} lowercase words.')
print(f'There are {numeric:>2} numeric strings.')
print(oddelovac)

delka = sorted(pocet)
x = 0
while x < len(delka):
    lg = delka[x]
    freq = pocet[lg]

    if len(str(lg)) == 1:
        index = ' ' + str(lg)
    else:
        index = str(lg)

    print(index, '*' * freq, freq)
    x = x + 1
print(oddelovac)
print(f'If we summed all the numbers in this text we would get: {all_numb}')
print(oddelovac)
