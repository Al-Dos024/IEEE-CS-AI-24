try:
    with open('Task2/text.txt') as txt:
        print(txt.read())
except FileNotFoundError:
    print("That file not found")