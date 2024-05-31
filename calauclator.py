    first=int(input("enter the first number\n"))
    second=int(input("enter the second number\n"))
    opearator=input("enter an opearator ( + - * % / )\n")
    if opearator == '+':
           print(first + second)
    elif opearator == '-':
            print(first - second)
    elif opearator == '*':
            print(first * second)
    elif opearator == '%':
            print(first % second)
    elif opearator == '/':
            print(first / second)
    else:
        print("please enter valid input with operators and operands")