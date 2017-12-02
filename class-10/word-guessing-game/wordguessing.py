import random
import string

alphabeth = string.ascii_letters[:26]

def import_words(n):
    words = []
    with open('words.txt', 'r') as f:
        line = f.readline()
        while (line):
            if (len(line.strip('\n')) == n):
                words.append(line.strip('\n'))
            line = f.readline()
    return words

def valid_guess(letter, guessed_letters):
    # YOUR CODE GOES HERE
    return True

def guess_progress(letter, secret_word, word_progress):
    # YOUR CODE GOES HERE
    return ""

def progress_format(word):
    formatted_word = ""
    for letter in word:
        formatted_word += letter + " "
    return formatted_word

def main():
    print("Starting game!\n")

    print("""The rules of the game are:
    
    1. The computer chooses a random word
    2. You will try to guess the letters in the word one by one
    3. You are allowed to miss 6 times, after that you lose the game
    4. You win by guessing all letters correctly
    
Good luck!\n\n
    """)
    n = int(input("How long would you like the word to be? "))
    words = import_words(n)
    playing = True
    # main loop
    while (playing):
        # secret_word = random.choice(words)
        secret_word = "wow"
        word_progress = ''.join(['_' for _ in range(len(secret_word))])
        wrong_guesses = 0
        guessed_letters = []
        while (wrong_guesses < 6 and word_progress != secret_word):
            display_word_progress = progress_format(word_progress)
            print("Progress: {}, Guessed letters: {} Incorrect Guesses left: {}"
                  .format(display_word_progress, guessed_letters, 6 - wrong_guesses))
            guess = input("Guess a letter: ")
            if valid_guess(guess, guessed_letters):
                guessed_letters.append(guess)
                if guess in secret_word:
                    word_progress = guess_progress(guess, secret_word, word_progress)
                else:
                    print("Sorry the letter is not in the word.")
                    wrong_guesses += 1
        if wrong_guesses == 6:
            print("Sorry you lost, the secret word was: " + secret_word)
        elif word_progress == secret_word:
            print("Congratulations you won! The word was: {}".format(secret_word))

        again = input("Would you like to play again?")
        if again[0] != 'y':
            playing = False
            print("Okay, goodbye!")




if __name__ == "__main__":
    main()
