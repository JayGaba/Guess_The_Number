import random
a = random.randint(1,100)
print("The mystery number lies between 1 to 100. You have 5 chances to correctly guess it.")
i = 0


def guess():
    while i < 5:
        b = int(input("Enter your guess: "))
        i = i+1
        if b > a:
            print("The number entered is higher.")
            print("You have ", 5-i, "more tries left")
        elif b < a:
            print("The number entered is lower.")
            print("You have ", 5 - i, "more tries left")
        else:
            print("Correct guess!")
            again()
            break
        if(5-i) == 0:
            again()


def again():
    cal_again = input("Do you want to play again?\nPress 'y' for YES and 'n' for NO: " )
    if cal_again == 'y':
        guess()
    else:
        print("See you again!")


guess()
