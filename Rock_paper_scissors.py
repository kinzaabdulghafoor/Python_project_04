import random


# function to make the computer choose
def computer_choice():
    choics = ["rock", "paper", "scissores"]
    return random.choice(choics)

# function to decide who wins
def decide_winner(user_choice, computer_choise):
    if user_choice == computer_choice:
        return "its a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors")  or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
         return "you win!"
    else:
        return "computer win!"


# game loop
while True:
    user_choice = input("enter your choice (rock, paper, scissors): ").lower() 

    if user_choice not in ["rock", "paper", "scissors"]:
       print("invalid choice! please choose again.")
       continue

    comp_choice = computer_choice()
    print(f"computer chose: {comp_choice}")


    result = decide_winner(user_choice, comp_choice)
    print(result)


    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("thanks for playing!")
        break                     
