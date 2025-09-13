#Number Guessing Game(Guess It!) 
import random

print("\n Python Number Guessing Game :-->")
print("Complete all 3 levels to win!\n")

levels = {1: 10, 2: 50, 3: 100}  # Levels

for level in range(1, 4):  # Loop for levels
    start = 1
    end = levels[level]
    snum = random.randint(start, end)
    c = 0
    game_active = True

    print(f"\n<--- Level {level} --->")
    print(f"Select a number between {start} and {end}")

    while game_active:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            c += 1

            if guess < start or guess > end:
                print("That number is out of range")
            elif guess < snum:
                print("Too low! Try again")
            elif guess > snum:
                print("Too high! Try again")

            # Smart hints every 3 wrong attempts
            if c % 3 == 0 and guess != snum:
                if abs(snum - guess) <= 5:
                    print("Almost there!")
                elif abs(snum - guess) <= 15:
                    print("You're on the right track.adjusting required.")
                else:
                    print("....Off track! Rethink")

            # Correct guess
            if guess == snum:
                print(f"\n Correct! The secret number was {snum}")
                print(f" Number of attempts: {c}")

                # Save score to leaderboard
                with open("leaderboard.txt", "a") as f:
                    f.write(f"Level {level}: Guessed {snum} in {c} attempts\n")

                print(" Score saved to leaderboard.txt")
                game_active = False

        else:
            print("Invalid Guess ")
            print(f"Please select a number between {start} and {end}")

# After finishing all 3 levels
print("\n Congratulations! You completed all levels of the game!")
#this is your leaderboard..
print("\n Leaderboard so far:")
try:
    with open("leaderboard.txt", "r") as f:
        scores = f.readlines()
        if scores:
            for line in scores:
                print(line.strip())
        else:
            print("No scores yet.")
except FileNotFoundError:
    print("No leaderboard found yet.")
