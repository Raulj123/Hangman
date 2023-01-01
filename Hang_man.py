import random


words = ["DOBY", "MAYA", "JACK", "MAX", "MIKO"]
ran_word = random.choice(words)

name = input("What is your name:  ")
print("Be ready to play some Hangman " + name)

right = ['*'] * len(ran_word)
count = 0
wrong = []
guessed_corr = []
answer = "Y"

while count < 3:
    output = ''
    # if you choose right letter

    # for each letter in ran_word
    for letter in ran_word:
        # if letter is in guess
        if letter in guessed_corr:
            output += letter
        else:
            output += "*"

    if '*' not in output:
        print("You win the game!")
        break

    print("This is your word to guess:  ", output)
    guess = input("Enter a letter: ").upper()

    if guess in guessed_corr or guess in wrong:
        print("You already entered this")
    elif guess in ran_word:
        guessed_corr.append(guess)
    else:
        wrong.append(guess)
        count += 1

    if count == 0:
        print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif count == 1:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
    elif count == 2:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |         \n"
                  "__|__\n")
    elif count == 3:
        print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
