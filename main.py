import random

print("Welcome to the Rock - Paper - Scissors game!")

while True:
    moves = ["R", "P", "S"]
    player_move = (input("Please choose a move between: \n R for Rock \n P for Paper \n S for Scissors \n")).upper()
    cpu_move = random.choice(moves)
    
    while player_move not in moves:
        print("Error! Invalid move selected.")
        player_move = (input("Please choose a move between: \n R for Rock \n P for Paper \n S for Scissors \n")).upper()
    
    if player_move == "R" and cpu_move == "P":
        print("Player (Rock) : CPU (Paper)")
        print("Paper covers rock. Computer wins!")
    elif player_move == "R" and cpu_move == "S":
        print("Player (Rock) : CPU (Scissors)")
        print("Rock smashes scissors. You win!")
    elif player_move == "P" and cpu_move == "R":
        print("Player (Paper) : CPU (Rock)")
        print("Paper covers rock. You win!")
    elif player_move == "P" and cpu_move == "S":
        print("Player (Paper) : CPU (Scissors)")
        print("Scissors cuts paper. Computer wins!")
    elif player_move == "S" and cpu_move == "P":
        print("Player (Scissors) : CPU (Paper)")
        print("Scissors cuts paper. You win!")
    elif player_move == "S" and cpu_move == "R":
        print("Player (Scissors) : CPU (Rock)")
        print("Rock smashes scissors. Computer wins!")
    elif player_move == "S" and cpu_move == "S":
        print("Player (Scissors) : CPU (Scissors)")
        print("It's a tie! Try again")
    elif player_move == "R" and cpu_move == "R":
        print("Player (Rock) : CPU (Rock)")
        print("It's a tie! Try again")
    else:
        print("Player (Paper) : CPU (Paper)")
        print("It's a tie! Try again")
    
    if player_move != cpu_move:
        break

print("Thank you for playing, have a nice day :)")