import random
playing = True
number = str(random.randint(20,100))
print("I will generate a number from 20 to 100, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
print("Good Luck")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game.")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, Good Luck for next time. \n")