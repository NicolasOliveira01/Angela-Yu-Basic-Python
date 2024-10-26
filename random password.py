import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range(0, nr_letters):
    password.append(random.choice(letters))
# gera letras aleatórios na quantidade que o usuário escolheu

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))
# gera simbolos aleatórios na quantidade que o usuário escolheu

for char in range(0, nr_numbers):
    password.append(random.choice(numbers))
# gera números aleatórios na quantidade que o usuário escolheu

"""print(password)
random.shuffle(password) # embaralha a ordem dos itens em uma lista
new_password = ""
for char in password:
    new_password += char
print(new_password)"""

length = []
for i in range(len(password)):
    length.append(i)
# gera uma lista que cada elemento é o indice de password (letras, simbolos e números)
#print(length)
#print("--------------------------------")

new_password = ""
while password:
    index = random.randint(0, len(password) - 1)
    print(password)
    element = password.pop(index)
    new_password += element
    print(new_password)
    print("--------------------------------")
print(new_password)

# exemplo password → ['X', 'F', ')', '#', '7']
# exemplo length → [0, 1, 2, 3, 4]
# index → gera um índice aleatório e a cada loop a lista diminui (`pop`) e index sempre vai gerar um número que seja um valor válido do tamanho da lista na análise