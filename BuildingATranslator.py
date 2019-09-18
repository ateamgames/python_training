def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase:  ")))

# this program will replace any vowel with the letter G
