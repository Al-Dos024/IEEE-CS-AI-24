import random
secret_number = random.randint(1, 100)
win = False
Try = 0
print("I have chosen a number between 1 and 100. you have 5 tries guess it! ")

while (Try < 5):
    guess = int(input("Enter your guess : "))
    Try += 1

    if guess < secret_number:
        print(f"Too low! Try guessing a higher number, try number {Try}")
    elif guess > secret_number:
        print(f"Too high! Try guessing a lower number,  try number {Try}")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")
        print(f"It took you {Try} attempts.")
        win = True
        break
if win is False:
    print(f"You didt get it :( , it was {secret_number}")


