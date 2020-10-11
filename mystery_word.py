from random import choice

NUM_TURNS = 8
WORDS_FILE = "words.txt"



def check_victory(letters_guessed, letters_to_guess):
    return letters_to_guess <= letters_guessed

def show_guessed_so_far(word_toguess, letter_guessed):
    output = ''
    for letter in word_toguess:
        if letter in letter_guessed:
            output += letter + " "
        else:
            output += '_ '
    print(f'Guessed so far: {output}')

def get_guess(letters_guessed):
    """
    1. Gets a guess as input from the user
    2. Set up a validation loop on the input
        2a. check alphabetical
        2b. check length of 1
        2c. Check if already guessed - i.e. is in letter_guessed
    3. return input
    """
    guess = input("Enter a letter: ")
    while (not(guess.isalpha()) or len(guess) > 1 or (guess in letters_guessed)):
        guess = input("Enter a letter: ")
    return guess


def play_game(word_to_guess):
    """
    1. Initialize the game state based on `word_to_guess`.
        1a. Create a set of letters that need to be guessed.
        1c. Set the number of guesses used to 0.
    
    2. Print the length of `word_to_guess`
    
    3. While the number of guesses used is less than `NUM_TURNS`:
        1b. Create an empty set of letters that have been guessed.
        3a. Show the user what they've guessed so far
        3b. Get a new user guess
        3c. Check whether the new user guess is an element of words to be guessed.
            3bi. If yes, let the user know that they guessed correctly
            3bii. Otherwise let the user know they guessed incorrectly and add 1
        3d. Check if the user has guessed all the ltters in the word.
            3di. If yes, print a victory message.
        4. Print a message indicating the user lost and revealing the word
            3dii. If no, continue at the top of the loop.
        5. Exit from the function (no return)
    """
    letters_to_guess = set(word_to_guess)
    letters_guessed = set()
    guesses_used = 0

    print(f"Your word has {len(word_to_guess)} letters.")

    while guesses_used < NUM_TURNS:
        show_guessed_so_far(word_to_guess, letters_guessed)
        
        new_guess = get_guess(letters_guessed)

        letters_guessed.add(new_guess)

        if new_guess in letters_to_guess:
            print("Correct!")

        else:
            print("Incorrect!")
            guesses_used += 1

        user_has_won = check_victory(letters_guessed, letters_to_guess)

        if user_has_won:
            print("Congratulations, you win!")
            print(f"You finished in {guesses_used} turns!")
            return

    # assert guesses_used == NUM_TURNS
    print("You lose!")
    print(f"Your word was {word_to_guess}")
    return




def read_words(filename):
    """
    1. Open the file for reading.
    2. Read in all the contents of the file of a string
    3. Split the string using newline characters
    4. return the list
    """
    with open(filename) as text_file:
        words = text_file.read()
        return words.split('\n')



def filter_by_difficulty(words, desired_difficulty):
    """
    HINT: use list comprhenesions and chained comparisons (e.g. 5 < x < 6)
    1. Check value of desired_difficulty
        1a. If 'easy', filter from `words` all words whose length is less than 4 or greater than 6.
        1b. If 'normal, filter for wards length 6-8
        1c. hard - length >= 8
    2. return filtered word list
    """
    if desired_difficulty == 'easy':
        filtered_words = [w for w in words if 4 <= len(w) <= 6]
    elif desired_difficulty == 'normal':
        filtered_words = [w for w in words if 6 <= len(w) <= 8]
    else:
        filtered_words = [w for w in words if 8 <= len(w)]
    return filtered_words

def get_word_to_guess(desired_difficulty):
    """
    1. Read all words from words.txt
    2. Check value of desired_difficulty
        2a. 'easy' - filter all words whose length is less than 4 or greater than 6
        2b. 'normal' - length 6-8
        3b. 'hard' - length >= 8
    3. Return a word at random from the list obtained in step 2
    """
    words = read_words(WORDS_FILE)
    filtered_words = filter_by_difficulty(words, desired_difficulty)
    return choice(filtered_words)

def get_user_difficulty():
    """
    1. Setup an input validation loop
    2. While user input is not valid
        2a. ask for the user input(normalized to lowercase)
        2b. Check that the user input is 'easy', 'normal', or 'hard'
        2c. Otherwise, return the user input 
    """
    user_input = input("Enter the difficulty: 'easy', 'normal', or 'hard' ").lower()
    while user_input != 'easy' and user_input != 'normal' and user_input != 'hard':
        user_input = input("Difficulty must be: 'easy', 'normal', or 'hard' ").lower()
    return user_input


def prompt_play_again():
    user_input = input("Would you like to play again? 'Yes or No': ").lower()
    
    while user_input != 'yes' and user_input != 'no':
        user_input = input("Would you like to play again? 'Yes or No': ").lower()
    
    return user_input == 'yes'
         
def run_game_loop():
    """
    1. Get desired user difficulty (easy, normal, or hard)
    2. Get a word for the player to guess.
    3. Play the game.
    4. Ask if the user wants to play again.
        a. If yes, rerun game loo
        b. Otherwise, exit the program
    """
    desired_difficulty = get_user_difficulty()
    word_to_guess = get_word_to_guess(desired_difficulty)
    play_game(word_to_guess)

    play_again = prompt_play_again()

    if play_again:
        run_game_loop()
    else:
        print("Thanks for playing")
        exit(0)

def main():
    """
    Run the game loop
    """
    "Welcome to my Mystery Word Game"
    run_game_loop()







if __name__ == "__main__":
    main()

