import random


words = ["python", "laptop", "gaming", "cloud", "matrix"]


word = random.choice(words)
word_letters = list(word)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.\n")


while incorrect_guesses < max_attempts:
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    
    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    
    if guess in word:
        print("✅ Correct!\n")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!\n")


if incorrect_guesses == max_attempts:
    print("\n💀 Game Over! The word was:", word)
