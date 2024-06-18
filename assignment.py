# A python programme that prompts a user to enter a letter then checks whether
# it is a consonant or a vowel.
# A python programme to check whether a number is prime or odd



def check_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"

    if len(letter) == 1 and letter.isalpha():
        if letter in vowels:
            return f"The letter '{letter}' is a vowel."
        else:
            return f"The letter '{letter}' is a consonant."
    else:
        return "Please enter a single alphabet letter."

def main():
    letter = input("Enter a letter: ")
    result = check_vowel_or_consonant(letter)
    print(result)

if __name__ == "__main__":
    main()
