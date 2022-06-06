import random
from re import S


print("This is a simple game of Rock Paper Scissors. Videlle says, 'Enjoy!'")

print(' ')
print(' ')

r_p_s = ["R", "P", "S"]


while True:
    for x in r_p_s:
        
        user_input = input("Select an option between 'R', 'S', 'P': \n")
        
        if user_input not in r_p_s:
            print ("Invalid option, please enter a valid input.")

        else: 
            print("Please hold on for your opponent")
            break
 
    comp_input = random.choice(r_p_s)

    print(f"\nPlayer {user_input} : CPU {comp_input}.\n")

    if user_input == comp_input:
        print(f"Both players selected {user_input}. It's a tie! Try again")
    elif user_input == "R":
        if comp_input == "S ":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "P":
        if comp_input == "R":
            print("Paper covers rock! You win!.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "S":
        if comp_input == "R":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
           


    choice = input('Would you like to play again? Yes(y)/No(n): \n')
        
    if choice == "y":
        pass
    if choice == "n":
        False
        print (" ")
        print ("Thanks for playing!")
        break

