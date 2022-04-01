"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    if 0 <= score <= 100:
        if score < 50:
            return "Bad"
        elif 50 <= score < 90:
            return "Good"
        else:
            return "Excellent"
    else:
        return "Invalid score"


if __name__ == '__main__':
    main()
