def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = []
    print("Print 5 numbers")
    for i in range(0, 5):
        numbers.append(int(input(f"Number {i + 1}: ")))
    print(f"Sum of all numbers is {sum(numbers)}")
    print(f"Average of all numbers is {sum(numbers) / len(numbers)}")
    print(f"Max number in numbers is {max(numbers)}")
    print(f"Min number in numbers is {min(numbers)}")
    username = input("What's your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
