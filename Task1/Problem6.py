def sum_even_numbers(n):
    sum_even = 0
    for num in range(2, n + 1, 2):
        sum_even += num
    return sum_even

def main():
    n = int(input("Enter a positive integer: "))
    result = sum_even_numbers(n)
    print(f"The sum of even numbers from 1 to {n} is {result}")

if __name__ == "__main__":
    main()
