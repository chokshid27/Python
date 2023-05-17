def is_vowel(char):
    """
    This function checks if a passed letter is a vowel or not.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels:
        print(char, "is a vowel")
    else:
        print(char, "is not a vowel")

# example :
is_vowel('a') # output: a is a vowel
is_vowel('b') # output: b is not a vowel
