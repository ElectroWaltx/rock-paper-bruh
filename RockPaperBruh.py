import random
switch = True
playagain_yes = ["yes","y","yeah","yea","ok","ya","yep"]
playagain_no = ["no", "n", "na", "nope","nah"]
options = ["rock","paper","scissors"]

def game(options):
    inp = input("Please enter your choice: ")
    compchoice = options[random.randint(0,2)]
    mychoice = inp.lower()
    while mychoice not in options:
        print("That's an invalid choice! Please enter 'rock', 'paper' or 'scissors'")
        inp = input("Please enter your choice: ")
        mychoice = inp.lower()
        print("Your choice: " + mychoice)
    print("Your choice: " + mychoice)
    print("Computer's choice: " + compchoice)
    if compchoice == mychoice:
        print("Tie")
    elif compchoice == "rock" and mychoice == "scissors":
        print("You Lose")
    elif compchoice == "rock" and mychoice == "paper":
        print("You Win!")
    elif compchoice == "paper" and mychoice == "scissors":
        print("You Lose")
    elif compchoice == "paper" and mychoice == "rock":
        print("You Win!")
    elif compchoice == "scissors" and mychoice == "paper":
        print("You Lose")
    elif compchoice == "scissors" and mychoice == "rock":
        print("You Win!")
        

def play_again(playagain_yes,playagain_no):
    playagain = input("Do you want to play again?: ")
    if playagain in playagain_yes:
        switch = True
    elif playagain in playagain_no:
        switch = False
        print("Thanks for playing!")
        exit(0)
    else:
        print("Not a valid input.")
        exit(0)
        switch = False

while switch == True:
    game(options)
    play_again(playagain_yes,playagain_no)  


