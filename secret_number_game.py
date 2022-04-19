print("SECRET NUMBER \n")                       # dodati: 1) bodovanje i praćenje bodova  2) bonus za 20 bodova - pomoć je li broj (ne)paran
                                                # 3) za pogodak isprve dati duple bodove
player_name = input("enter your name: ")        
difficulty = input("Choose difficulty:\n"       #choose difficulty
                   " easy (1 - 10), \n"        
                   "normal (1 - 20) \n"
                   "or hard? (1 - 50)")
if difficulty == "easy":
    numbers_range = list(range(1, 11))      # each difficulty has a max number that you can guess
    max_choice = 10
    win_points = 1
elif difficulty == "normal":
    numbers_range = list(range(1, 21))
    max_choice = 20
    win_points = 2
elif difficulty == "hard":
    numbers_range = list(range(1, 51))
    max_choice = 50
    win_points = 5


def play_secret_number():
    import random

    secret_number = random.choice(numbers_range)
    user_guess = ""
    number_of_guesses = 0
    print(secret_number)   # debug

    while user_guess != secret_number:
        number_of_guesses += 1
        user_guess = int(input(f"pick a number between 1 and {max_choice}"))
        if user_guess == secret_number:
            print("congratulations! \n"
                  f"the secret number was {secret_number} \n"
                  f"you took {number_of_guesses} tries \n"
                  f"you won {win_points} points")
        elif user_guess > max_choice or user_guess < 1:                                       # checks that user has entered a number from allowed range
            print(f"{user_guess} is not a number between 1 and {max_choice}. try again")      # this is where max number helps us
        else:
            if user_guess < secret_number:
                print("too low, try again")
            elif user_guess > secret_number:
                print("too high, try again")


again = True

play_secret_number()

while again:
    repeat = input(f"{player_name}, do you want to play again? (Type yes or no.) \n")           # dodati kontrolu unosa za ostale stvari
    if repeat == "no":
        again = False
        print("\n Game ended. \n")
    else:
        play_secret_number()
