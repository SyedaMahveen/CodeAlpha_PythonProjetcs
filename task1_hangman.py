import random

def hangman():
    words = ["apple", "banana", "orange", "grapes", "mango"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman Game!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Show current progress
        progress = ""
        for letter in word:
            if letter in guessed_letters:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("❌ You lost! The word was:", word)

hangman()
