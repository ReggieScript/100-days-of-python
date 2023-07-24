import random

logo='''
 ____ _   _ ____     ___ __  __ ____ ___ ___     ___   __   __  __ ____/\
(_  _| )_( | ___)   / __|  )(  | ___) __) __)   / __) /__\ (  \/  | ___)(
  )(  ) _ ( )__)   ( (_-.)(__)( )__)\__ \__ \  ( (_-./(__)\ )    ( )__)\/
 (__)(_) (_|____)   \___(______|____|___(___/   \___(__)(__|_/\/\_|____|)
'''

number=random.randint(1,100)

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
dif=input("Choose a difficulty, 'easy' or 'hard'.\n")

if dif=='easy':
    attempts=10
else:
    attempts=5

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess= int(input("Make a guess.\n"))
    if guess==number:
        print(f"You got it! The answer was {number}")
        break
    elif guess>number:
        print("Too high")
        attempts=attempts-1
    elif guess<number:
        print("Too low")
        attempts=attempts-1
if attempts==0:
    print("You've run out of attempts. You lose :(")
    print(f"The correct answer was {number}")
    