import random


def main():
    lines = []
    amount_of_picks = int(input("How many quick picks? "))
    for i in range(amount_of_picks):
        line = []
        for j in range(6):
            number_to_add = random.randint(1, 45)
            while number_to_add in lines:
                number_to_add = random.randint(1, 45)
            line.append(number_to_add)
        lines.append(sorted(line))
    display_picks(lines)


def display_picks(lines):
    for line in lines:
        for number in line:
            print(f"{number:2}", end=" ")
        print("")


if __name__ == '__main__':
    main()
