import random

from hangman_words import word_list
from hangman_art import stages, logo
# jeito de importar uma variável de outro arquivo sempre precisar passar
# {nome_arquivo}.variável

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    # dentro do while o display sempre vai começar vazio (””), se o primeiro guess do usuário (letra) tiver na chosen_word o primeiro for vai printar aonde aparece o guess e as outras letras vai colocar o "_"
    # Depois ele vai colocar o guess (letra) dentro da lista correct_letters
    # chosen_word="aardvark" = aa_ _ _a_ _
    # Depois desse print, como ainda tem "_" ele volta para o início do while e começa o mesmo processo com o display vazio (””). Imagine que o outro guess foi r, ele não entra no if mas entra no elif porque "a"
    # (primeiro valor de letter) está em correct_letters então ele adiciona "a" em display
    # Quando letter for r o valor do display será aa_ e neste caso entra no if, adicionando r no display (aar) e colocando r em correct_letters

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
