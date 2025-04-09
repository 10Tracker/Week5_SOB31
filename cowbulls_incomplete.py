import random

def compare_numbers(number, user_guess):
    cow = 0  # Initializing variables cow and bull
    bull = 0  

    for i in range(len(number)): # loops to every number with the same index in variable user_guess and number
        if user_guess[i] == number[i]:  # Checks whether the number matches corresponding to its index.
            bull += 1
        elif user_guess[i] in number:  # Checks whether the numerical values match in 2 variables.
            cow += 1

    return (cow, bull)  # Returns values containing the number of cows and bulls
playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " try! The number was "+str(number)) # answer will only be shown in the end
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
