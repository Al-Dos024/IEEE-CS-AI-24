def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    print("Reversed sentence:", reversed_sentence)

if __name__ == "__main__":
    main()
