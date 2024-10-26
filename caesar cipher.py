
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    # precisa estar fora no for, porque no caso de "decode" vai ter um erro, porque no
    # shift_amount entra no if e fica negativo e a próxima letra também vai entrar no
    # "decode" deixando positivo, mudando o resultado "output_text"

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    # encode → o deslocamento é positivo (vai pra frente) e o decode é negativo (vai pra trás)
    # .index() → retorna o índice do parâmetro passado na lista
    # shifted_position %= len(alphabet) → uma forma de nunca dar um número > que len(alphabet), porque na teoria se for maior ele teria que voltar para o início da lista, então o %= vai retornar exatamente o índice da letra
    # se shifted_position for menor que len(alphabet), vai retornar o shifted_position
    # 12 %= 26 → 12

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

        