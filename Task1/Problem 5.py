def is_palindrome(word):
    # Reverse the word
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

def main():
    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")

if __name__ == "__main__":
    main()
