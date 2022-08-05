import random
import time

# x is the integer guessed
x: int = 0
low: int = 1
high: int = 1000
limit = 0
player_number = 0
cpu_guess = 0
guesses = 0
Still_Guess = True
Valid_Guess = False
Valid_Limit = False

print("Hello!")

# Have the user input a number and a total guess count
time.sleep(1)
while not Valid_Guess:
    try:
        player_number = int(input("Give me a number between " + str(low) + " and " + str(high) + ": "))
        if low > player_number or player_number > high:
            print("That isn't between " + str(low) + " and " + str(high) + "!")
        else:
            Valid_Guess = True
    except ValueError:
        print("Hey! That's not a number!")

time.sleep(1)
while not Valid_Limit:
    try:
        limit = int(input("Okay! How many guesses do I have? "))
        Valid_Limit = True
    except ValueError:
        print("Hey! That's not a number!")
time.sleep(1)
print("I am going to guess your number in " + str(limit) + " guesses!")

# While the random number generated is not equal to the player's guess, continue this loop

while x != player_number and guesses < limit:
    x = random.randint(int(low), int(high))
    guess = input("Is " + str(x) + " your number? ").lower()
    if guess == "no":
        cpu_guess = input("Is your number higher or lower than " + str(x) + "? ").lower()

        if cpu_guess == "higher":
            if player_number < x:
                print("I don't think you're telling me the truth...")
                continue
            else:
                low = int(x)
                x = random.randint((int(low) + 1), int(high))
                guesses = int(guesses + 1)
                continue

        elif cpu_guess == "lower":
            if player_number > x:
                print("I don't think you're telling me the truth...")
                continue
            else:
                high = int(x)
                x = random.randint(int(low), (int(high) - 1))
                guesses = int(guesses + 1)
                continue

        else:
            print("Hey! No cheating! I get another guess now!")
            continue
    elif guess == "yes":
        print("Are you sure? I don't think I know your number yet.")
        continue
    else:
        print("Sorry, I didn't understand that.")
        continue
while x != player_number and guesses >= limit:
    time.sleep(1)
    print("I'm out of guesses :( You win")
    time.sleep(1)
    print("Your number was " + str(player_number) + " and my last guess was " + str(x))
    time.sleep(1)
    print("I was " + str(abs(x - player_number)) + " off.")
    break

while x == player_number and guesses < limit:
    win = input("Is " + str(x) + " your number? ").lower()
    if win == "yes":
        print("Woohoo! I win!")
        break
    else:
        print("Are you sure? I think I have it")
        continue
