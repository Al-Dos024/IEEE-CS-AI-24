def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = int(input("Enter number : "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        print("Factorial of", num, "is", factorial(num))

if __name__ == "__main__":
    main()