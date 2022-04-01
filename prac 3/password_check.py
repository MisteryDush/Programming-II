MINIMUM_LENGTH = 4
MAX_LENGTH = 8


def get_password(minimum_length, max_password):
    password = input("Enter the password: ")
    while len(password) < minimum_length or len(password) > max_password:
        print(f"Password needs to be at least {minimum_length} characters")
        password = input("Enter the password: ")
    return password


def print_asterisks(asterisks):
    print('*' * len(asterisks))


def main():
    password = get_password(MINIMUM_LENGTH, MAX_LENGTH)
    print_asterisks(password)


if __name__ == '__main__':
    main()