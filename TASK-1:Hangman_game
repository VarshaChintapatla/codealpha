
import random

# List of words
word_list = ["python", "javascript", "hangman", "computer", "science", "programming"]

# Select a random word
word = random.choice(word_list)
word_display = ["_"] * len(word)  # Hidden word representation
attempts = 6  # Maximum incorrect guesses allowed
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(word_display))

while attempts > 0 and "_" in word_display:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Incorrect! Attempts left: {attempts}")

    print(" ".join(word_display))


if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
