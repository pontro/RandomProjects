import random, os
from words import words
import string
from hangman_visual import lives_visual_dict

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')

def choose_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = choose_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = len(lives_visual_dict) - 1

    while len(word_letters) > 0 and lives > 0:
        print('lives = ' + str(lives))

        print('You have', str(lives), 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('\nYour letter,', user_letter, 'is not in the word.')
                lives -= 1
        elif user_letter in used_letters:
            print("You already have guessed that letter. Try again") 
        else:
            print('Invalid character. Try again')
        clear_screen()

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
    

hangman()