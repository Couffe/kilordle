from words import WORDLES, WORDS
from kilowordle import kilowordle

length = 1000
game = kilowordle(WORDLES, WORDS, length)
quit = False
while not quit:
    guess = input("Input a 5 letter word: ").lower()
    if (guess == "q" or guess == "quit"):
        quit = True
        break
        
    if not game.guess(guess):
        print(f"{guess} is not a valid word!")
    elif game.solved == length:
        quit = True
        print(f"You won in {len(game.guesses)} guesses!")
        break
    else:
        game.print()
        print(f"Solved {game.solved} / {length} | {length - game.solved} remaining...")
        print()

