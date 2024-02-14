try:
    user_input = input("Please enter a number: ")
    num = int(user_input)
    print("You Entered:", num)
except ValueError:
    print("Please enter a valid number.")
