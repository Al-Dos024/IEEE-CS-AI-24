def is_perfect_number(n):
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

def main():
    num = int(input("Enter a positive integer: "))
    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

if __name__ == "__main__":
    main()
