import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
# coloca as 'imagens' dentro de uma lista

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))
# transforma a escolha do usuário em int para poder usar como indice
# a sua escolha vai representar o indice da 'imagem' na lista

print(f'Your choice is:\n {game_images[user_choice]}')

computer_choice = random.randint(0, 2)
# escolhe aleatoriamente rock, paper, scissors
print(f"The computer's choice is:\n {game_images[computer_choice]}")

if user_choice >=3 or user_choice < 0: # escolher outro número sem ser 0,1,2
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2: # Rock(User) x Scissors(Computer)
    print("You win!")
elif computer_choice == 0 and user_choice == 2: # Rock(Computer) x Scissors(User)
    print("You lose!")
elif computer_choice > user_choice: # forma mais fácil de representar duas derrotas
    print("You lose!")
elif user_choice > computer_choice: # forma mais fácil de representar duas vitorias
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")