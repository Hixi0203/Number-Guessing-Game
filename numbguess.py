import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("You have five chance to guess the coreect number")
    
    difficulties = {
        '1':('Easy', 10),
        '2':('Medium', 5),
        '3':('Hard', 3)
    }
    
    print("Please select the difficulty level:")
    print("1. Easy (10 chance)")
    print("2. Medium (5 chance)")
    print("1. Hard (3 chance)")
    
    choice = input("Enter your choice: ")
    
    if choice  not in difficulties:
        print("Invalid choice. Defaulting to Medium (5 chance).")
        choice = '2'
        
    difficulties_name, chance_left = difficulties[choice]     
    print(f"\nGreat! You have selected the {difficulties_name} difficulty level")
    print("Let's start the game!\n")
    
    secret_number = random.randint(1,100)
    attempts = 0
    
    while chance_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number: ")
            continue
        
        attempts += 1
        chance_left -= 1
        
        if guess == secret_number:
            print(f"Congratulations! You guesses the correct number in {attempts} attempts")
            return
        elif guess < secret_number:
            print(f"Incorrect the numer is greater than {guess}:")
        else:
            print(f"Incorrect! The number is less than {guess}")     
              
    print(f"\nYou've run out of chance! The correct number was {secret_number}.")     
    
if __name__ == "__main__": start_game()
             