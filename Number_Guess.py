from pathlib import Path
import random

def welcome():
    print("Welcome")
    print("This is Number Guessing game\n")
    print("1.Start")
    print("2.Score")
    print("3.Quit")


def game(level, score_multi, chance):
    print(f"Level: {level}")
    print(f"Score Multipler: {score_multi}")
    print(f"Chance: {chance}\n")
    print('─'*20)

    random_number = random.randint(1,100)
    while chance > 0:
        try:
            guess = int(input("Guess: "))

            if guess == random_number:
                print("Correct answer")

                score = (chance) * score_multi
                print(f"Score: {score}")
                return score

            elif guess > random_number:
                print("Try lower")

                if abs(guess - random_number) < 5:
                    print("You are close")
            else :
                print("Try higher")
                if abs(guess - random_number) < 5:
                    print("You are close")
            chance -=1
        except ValueError:
            print("Please Enter Value")
    
    print('─'*20)
    print("Game Over")
    print(f"Ther correct number was {random_number}") 
    print('─'*20)
    return 0 

running = True          
score = 0
user_name = ''  
file_name = Path("Score.txt")               
while running :
    if not file_name.is_file():
        with open(file_name, "a") as f:
            name = 'Name'
            score_label = 'Score'
            f.write(f"┌{"-"*43}┐\n")
            f.write(f"|{'':<15} Score Board {' ':<15}|\n")
            f.write(f"├{'-'*20}-+-{'-'*20}┤\n")
            f.write(f"|{name:<20} | {score_label:<20}|\n")
            f.write(f"├{'-'*20}-+-{'-'*20}┤\n")

            
    welcome()
    try:
        choice = int(input("Choice: "))
        match choice:
            case 1:
                user_name = input("Enter Your Name: ")

                print("1. Easy")
                print("2. Medium")
                print("3. Hard")
                try:
                    choice_inside = int(input("Choice: "))
                    match choice_inside:
                        case 1:
                            score = game(level='Easy', score_multi=1.25, chance=10)                            
                        case 2:
                            score = game(level='Medium', score_multi=2.5,chance=7)
                        case 3:
                            score = game(level='Hard', score_multi=5,chance=3)
                        case _:
                            print("Invalid Choice")
                except Exception as e:
                    print(f"Error: {e}")

                with open("Score.txt", "a") as file:
                    file.write(f"|{user_name:<20} | {score:<20}|\n")

            case 2:
                with open(file_name, 'r') as file:
                    score_text = file.read()
                    print(score_text)
            case 3:
                print("exiting...")
                running = False
            case _:
                print("Invalid choice\n")
    except ValueError:
        print("Error: Invalid Input")
    except Exception as e:
        print(f"Error: {e}")