# Hangman Game - Classic Word Guessing

# Banner art for a cool game start vibe
banner = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
'''
print(banner)

# List of words for the game – a mix of animals and common real-world objects
word_list = [
    'aardvark', 'baboon', 'camel', 'apple', 'banana', 'orange', 'guitar', 'house',
    'school', 'garden', 'pencil', 'mountain', 'river', 'friend', 'family',
    'window', 'bottle', 'cloud', 'flower', 'market', 'travel', 'mirror', 'blanket',
    'sunshine', 'holiday', 'animal', 'jungle', 'village', 'camera', 'pillow',
    'cookie', 'train', 'doctor'
]

# Hangman visuals for each wrong guess (from 0 to 6 wrong attempts)
Stages = [r"""
  +--+
  |  |
     |
     |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""]

# Step 1: Randomly select a word
import random
random_word = random.choice(word_list)

# Step 2: Create a display placeholder with blanks ( _ ) for each letter
place_holder = ''
for _ in random_word:
    place_holder += ' _ '
print(place_holder)

# Step 3: Game initialization variables
correct_letter = []  # To store all correctly guessed letters
game_over = False    # Flag to end the loop/game
lives = 0            # Counter for wrong guesses (max: 6)

# Step 4: Main game loop – continues until player wins or loses
while not game_over:
    # Ask user for a letter guess and convert to lowercase
    guess = input('What is your letter choice? ').lower()
    
    # Temporary display string to show progress after each guess
    display = ''
    
    # Step 5: Check each letter in the word
    for letter in random_word:
        if guess == letter:
            # Correct guess – show letter and store it
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            # Already guessed correctly before – keep showing it
            display += letter
        else:
            # Not guessed yet – show blank
            display += ' _ '

    # Step 6: Handle wrong guess
    if guess not in random_word:
        lives += 1
        print(Stages[lives])  # Show hangman stage for current life count
        if lives == 6:
            print('You lose! The word was:', random_word)
            break
    
    # Step 7: Print current state of word
    print(display)
    
    # Step 8: Check for win condition – no more blanks
    if ' _ ' not in display:
        print('You win! 🎉')
        game_over = True
