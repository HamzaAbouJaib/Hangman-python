import random
from words import words

#list of all letters in the alphabet
ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def pick_word():
    """
    If the word has a dash, a space, or is longer than 7 characters, pick another word.
    :return: The randomly selected word.
    """
    random_word = random.choice(words)
    while "-" in random_word or " " in random_word or len(random_word) > 7:
        random_word = random.choice(words)
 
    return random_word.upper()


def validate_user_guess():
    """
    Gets the user's input, then checks if the input is a single character and that character is a letter of the alphabet. 
    Keep asking for input until the conditions are met.
    :return: The user's guess
    """
    valid_guess = False
    while(not valid_guess):
        user_guess = input('Enter a letter: ').upper()
        if len(user_guess) == 1 and user_guess in ALPHABET:
            valid_guess = True
        else:
            print('Invalid input')
        print('')
    return user_guess


def user_progress(word, guessed_letters):
    """
    For each letter in the word, if the letter is in the guessed_letters list, add the letter to the
    word_progress string, otherwise add a dash to the word_progress string.
    
    :param word: the word that the user is trying to guess
    :param guessed_letters: a list of letters that the user has guessed
    :return: The word_progress variable is being returned.
    """
    word_progress = ''
    for letter in word:
        if letter in guessed_letters:
            word_progress += letter
        else: 
            word_progress += '-'

    return word_progress


def main(random_word):
    """
    The function takes a random word as an argument and returns True if the user guesses the word
    correctly, otherwise it returns False.
    
    :param random_word: The word that the user is trying to guess
    :return: a boolean value.
    """
    lives = 7
    game_over = False
    guessed_letters = []
    
    while(not(game_over) and lives > 0):
        # Displays the number of remaining lives
        print('\nYou have %(lives)d %(lives_spelling)s remaining' % dict(lives=lives, lives_spelling = 'life' if lives == 1 else 'lives'))

        # Displays the correctly guessed letters based on the last guess. 
        # Ex: if the user guessed 'A' and that was correct then it would display '--A---' assuming A is the 3rd letter in the word.
        print(user_progress(random_word, guessed_letters))

        # Gets a valid user guess
        user_guess = validate_user_guess()

        # checks if the letter the user guessed has been guessed before.
        if (user_guess in guessed_letters):
            print('You already guessed the letter %s' % user_guess)
            continue

        guessed_letters.append(user_guess)

        if(not(user_guess in random_word)):
            print('Incorrect guess\n')
            lives -= 1

        # Get a string of the correctly guessed letters after the latest guess.
        # If the string matches the randomly selected word then the user has won otherwise the game keeps going. 
        if (user_progress(random_word, guessed_letters) == random_word):
            game_over = True

    # If the game ended and the user did not use all their lives return true (user has won) otherwise return false (user has lost).
    if lives > 0:
        return True
    return False


play_again = 'Y'

while play_again == 'Y':
    random_word = pick_word()
    result = main(random_word)
    if result:
        print('You Won. The word was ' + random_word)
    else:
        print('You Lost. The word was ' + random_word)

    play_again = input('\n\n\nDo you want to play again? (y/n): ').upper()

print('Exiting game...')
