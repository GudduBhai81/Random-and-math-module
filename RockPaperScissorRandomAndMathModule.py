import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors) = ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_actions = random.choice (possible_actions)

    if user_action == computer_actions:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if  computer_actions == "scissors":
            print("Rock smashes scissor! Wow You won.")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if  computer_actions == "rock":
            print("Paper covers rock! Wow You won.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if  computer_actions == "paper":
            print("Scissors cuts paper! Wow You won.")
        else:
            print("Rock smashes scissor! You lose.")

    play_again = input("Do You Want To Play Again? (Y/N) = ")
    if play_again !="Y":
       break