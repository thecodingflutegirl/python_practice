from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    n1 = float(input('What is the first number? :'))
    for operation in operations:
        print(operation)

    calculating = True
    while calculating:
        operation_symbol = input('Pick an operation :')
        n2 = float(input('What is the next number? :'))
        calculation = operations[operation_symbol]
        answer = calculation(n1, n2)
        print(f'{n1} {operation_symbol} {n2} = {answer}')

        calculate_again = input(
            f'Type "y" to continue calculating with {answer}, type "n" to start a new calculation, or any key to exit:')
        if calculate_again == 'y':
            n1 = answer
        elif calculate_again == 'n':
            calculating = False
            calculator()
        else:
            calculating = False
            print('Thank you, goodbye!')


calculator()
