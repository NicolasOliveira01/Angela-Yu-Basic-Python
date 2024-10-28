from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}
# neste dicionário, as chaves (operadores) estão se referindo a função, depois usa o (parâmetro1, parâmetro2) para chamar a função
# Exemplo:
# addition_function = add -> Referência à função 'add' (sem parênteses)
# result_add = addition_function(5, 3) -> Aqui chamamos a função
# print(operations["+"]) -> <function add at 0x000001C40E0BE280>

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        # mostra todas as chaves (+,-,/,*) do dicionário
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        # o usuário vai escolher um operador e cada operador é uma chave do dicionário e cada operador tem como valor uma referência da sua função
        # operations[operation_symbol] -> referência da função que ele escolheu (add, subtract, divide, multiply)
        # (num1, num2) -> são os operadores da função escolhida
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
            # volta para o início do while, porém vai fazer o resultado anterior com algum operador e outro número, por isso num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
            # usa a recursão para voltar ao início da função e não dentro do while

calculator()