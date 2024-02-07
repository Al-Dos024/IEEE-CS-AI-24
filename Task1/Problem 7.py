def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor not in factors:
                factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def main():
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        factors = prime_factors(num)
        if len(factors) == 0:
            print("Prime factors: None")
        else:
            print("Prime factors:" , ' , '.join(map(str, factors)))
   

if __name__ == "__main__":
    main()
