import random
import hangman_stages
import words_file
print("Welcome to Hangman Game! \nLet's begin the game!!")
lives = 6
word = random.choice(words_file.word_list)
word = word.lower()
display = []
for i in range(len(word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ")
    for position in range(len(word)):
        letter = word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost!")
    if '_' not in display:
        game_over = True
        print("You win!")
    print(hangman_stages.stages[lives])
print("Play Again...")
