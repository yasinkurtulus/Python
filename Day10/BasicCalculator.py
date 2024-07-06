
def add(num_1, num_2):
    return num_1 + num_2
def subtract(num_1, num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2
def divide(num_1, num_2):
    return num_1 / num_2
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}
def calulator():
    finish = False
    num_1 = float(input("Enter a number: "))
    while not finish:
        for key in operations:
            print(key)
        symbol = input("Enter operation: ")
        operation = operations[symbol]
        num_2 = float(input("Enter a number: "))
        result = operation(num_1, num_2)
        print(f"{num_1} {symbol} {num_2} = {result}")
        answer = input("Would you like to continue? [y/n]: ")
        if answer == "n":
            finish = True
            calulator()
        num_1 = result
calulator()