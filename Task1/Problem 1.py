Arr = []
while True:
    num = int(input("Enter a number (enter -1 to End): "))
    if num == -1:
        break
    Arr.append(num)

if len(Arr) == 0:
    print("No numbers entered.")
else:
    largest = max(Arr)
    smallest = min(Arr)
    print("Largest number:", largest)
    print("Smallest number:", smallest)