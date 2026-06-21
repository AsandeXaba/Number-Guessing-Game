import random

def choice_selector(uppter_limit: int, text: str) -> int:
    while True:
        # This try clause is to check that the user enters a valid option
        try:
            number = int(input(text))
            # If the number is negative it is flagged
            if number < 0:
                print("Please enter a valid option.")
                continue
            # If a limit exits and the user exceeds the limit then it is also flagged
            elif number > uppter_limit:
                print("Please enter a valid option.")
                continue
            
            # return the number if none of the selection clauses are triggered
            return number
        
        # In the case a user enters something other than an integer/Number
        except ValueError:
            print(f"Please enter a valid number.")

def main():
    levels = ["Easy", "Medium", "Hard"]
    level_chances = [10, 5, 3]

    print("""Please select the difficulty level:
          1. Easy (10 chances)
          2. Medium (5 chances)
          3. Hard (3 chances)""")
    level = choice_selector(3, "Enter your choice: ")
    
    print(f"\nGreat! You have selected the {levels[level - 1]} difficulty level.\nLet's start the game.")
    
    random_number = random.randint(1, 100)
    chances = level_chances[level - 1]
    print(f"====You have {chances} chances. Let's get started.====\n")

    while True:
        for chance in range(1, chances + 1):
            guess = choice_selector(100, "Enter your guess: ")

            if guess > random_number:
                print(f"Incorrect! The number is less than {guess}")
            elif guess < random_number:
                print(f"Incorrect! The number is greater than {guess}")
            else:
                print(f"Congratulations! You guessed the correct number in {chance} attempts.")
                break

            print(f"You have {chances - chance} remaining chances...\n")
        else:
            print("Oops... You ran out of chances.\n")

        option = input("Would you like to play again(Y/N)? ").upper()
        if option == "Y":
            print("\nGreat! Let's go for another round...\n")
            continue
        print("\nThat was a great game, let's play again next time.\n=====Bye=====")
        break


if __name__ == "__main__":
    print("""Welcome to the Number Guessing Game!
            I'm thinking of a number between 1 and 100.
            You have 5 chances to guess the correct number.""")
    main()