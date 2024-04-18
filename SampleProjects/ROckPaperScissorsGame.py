import random

opts = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    algo = random.choice(opts)

    while player not in opts:
        player = input("Enter your choice(rock,paper,scissors):")

        print(f"Player picked: {player}")
        print(f"Algorithm picked: {algo}")

        if player == algo:
            print("It's a Tie")
        elif player == "rock" and algo == "scisscors":
            print("You Win!!")
        elif player == "paper" and algo == "rock":
            print("You Win!!")
        elif player == "scissors" and algo == "paper":
            print("You Win!!")
        else:
            print("You Lose- Better luck next time")

        play_again = input("Play again?(y/n): ").lower()
        if not play_again == "y":
            running = False

print("Thanks for playing :D ")
