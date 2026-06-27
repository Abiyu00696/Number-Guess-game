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
    



running = True          
score = 0
while running :
    welcome()
    try:
        choice = int(input("Choice: "))
        match choice:
            case 1:
                
                print("1. Easy")
                print("2. Medium")
                print("2. Hard")
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
            case 2:
                print("Score: ", score)
            case 3:
                print("exiting...")
                running = False
            case _:
                print("Invalid choice\n")
    except ValueError:
        print("Error: Invalid Input")
    except Exception as e:
        print(f"Error: {e}")