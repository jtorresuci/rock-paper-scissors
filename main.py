print("Let's play Rock, Paper, Scissors.\n")

while True:
    player1 = input("Player 1, Enter your choice: ")
    choice1 = ""
    againstr = "\nagain?\n"
    againstrerror = "\nagain?"

    # Check input player1
    if player1.upper() not in 'RPS':
        print("[ERROR: " + player1 + " not a valid move.]")
        again = input(againstrerror)
        if again == "y":
            print("")
            continue
        else:
            print("")
            print("Nice game!")
            break
    elif player1.upper() == 'R':
        choice1 = "Rock"
    elif player1.upper() == 'P':
        choice1 = "Paper"
    else:
        choice1 = "Scissors"
    
    player2 = input("Player 2, Enter your choice: ")

    choice2 = ""

    print(choice1 + " v.", end=" ")
    
    # Check input player2
    if player2.upper() not in 'RPS':
        print("[ERROR: " + player2 + " not a valid move.]")
        again = input("\nagain?")
        if again.lower() == "y":
            print("")
            continue
        else:
            print("")
            print("Nice game!")
            break
    elif player2.upper() == 'R':
        choice2 = "Rock"
    elif player2.upper() == 'P':
        choice2 = "Paper"
    else:
        choice2 = "Scissors"

    print(choice2)

    # Play Game
    p1wins = "Player 1 wins"
    p2wins = "Player 2 wins"

    player1 = player1.upper()
    player2 = player2.upper()

    if player1 == player2:
        print("It's a TIE")
        again = input(againstr)
        if again.lower() == "y":
            continue
        else:
            print("Nice game!")
            break
    elif player1 == 'R':
        if player2 == 'S':
            print(p1wins)
        else:
            print(p2wins)
    elif player1 == 'S':
        if player2 == 'P':
            print(p1wins)
        else:
            print(p2wins)
    elif player1 == 'P':
        if player2 == 'R':
            print(p1wins)
        else:
            print(p2wins)

    again = input(againstr)
    if again.lower() == "y":
        continue
    else:
        print("Nice game!")
        break