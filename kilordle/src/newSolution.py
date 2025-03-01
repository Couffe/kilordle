import itertools
import numpy as np
import pulp
from collections import defaultdict

def load_words(filename):
    """ Load words from file into a list. """
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def build_letter_position_mask(words):
    """ Build a 5 x 26 bitmask representing required letter positions. """
    letter_mask = np.zeros((5, 26), dtype=int)  # 5 positions, 26 letters
    
    for word in words:
        for pos, letter in enumerate(word):
            letter_mask[pos][ord(letter) - ord('a')] = 1  # Mark letter as required

    return letter_mask

def get_guess_mask(guess):
    """ Generate a bitmask for a given guess word. """
    guess_mask = np.zeros((5, 26), dtype=int)
    
    for pos, letter in enumerate(guess):
        guess_mask[pos][ord(letter) - ord('a')] = 1  # Mark guessed letter

    return guess_mask

def solve_minimum_guess_set(words, guesses):
    """ Solve ILP to find the minimal set of guesses that cover all letter positions. """
    print("Building bitmask representation...")
    letter_mask = build_letter_position_mask(words)
    
    print("Formulating ILP problem...")
    problem = pulp.LpProblem("Kilowordle_Letter_Cover", pulp.LpMinimize)

    # Decision variables: Binary (1 = use guess, 0 = don't use it)
    guess_vars = {g: pulp.LpVariable(f"guess_{g}", cat="Binary") for g in guesses}

    # Objective: Minimize number of selected guesses
    problem += pulp.lpSum(guess_vars[g] for g in guesses), "Minimize_Guesses"

    # Constraints: Cover all letter positions at least once
    for pos in range(5):  # Each position (0 to 4)
        for letter in range(26):  # Each letter (a-z)
            if letter_mask[pos][letter] == 1:  # Letter is required in this position
                covering_guesses = [
                    guess_vars[g] for g in guesses
                    if get_guess_mask(g)[pos][letter] == 1
                ]
                problem += pulp.lpSum(covering_guesses) >= 1, f"Cover_L{chr(letter+ord('a'))}_P{pos}"

    print("Solving ILP...")
    solver = pulp.COIN_CMD(path="/opt/homebrew/bin/cbc")  # Use CBC solver
    problem.solve(solver)

    # Extract selected guesses
    selected_guesses = [g for g in guesses if pulp.value(guess_vars[g]) == 1]

    return selected_guesses

if __name__ == "__main__":
    # Load words
    words = load_words("today.txt")
    guesses = load_words("guessable.txt")

    print(f"Loaded {len(words)} words and {len(guesses)} guessable words.")

    # Solve ILP for minimum guesses
    optimal_guesses = solve_minimum_guess_set(words, guesses)

    # Print results
    print("\nOptimal Guess Set:")
    for guess in optimal_guesses:
        print(guess)

    print(f"\nTotal guesses used: {len(optimal_guesses)}")
