# Import necessary functions
import time
from words import WORDLES, WORDS

def seedRandom(numWordles):
    pstNow = time.time() - 2880
    return pstNow // 86400

def genWorldList(wordles, length=1000):
    """ Generate a list of words using the generator algorithm. """
    numWordles = len(wordles)
    wordList = []
    generator = 163
    random = seedRandom(numWordles)
    
    for i in range(length):
        wordList.append(wordles[int((random + generator * i) % numWordles)])
        
    return wordList

def save_word_list_to_file(wordles, filename="today.txt", length=1000):
    """ Generate a word list and save it to a file with each word on a new line. """
    word_list = genWorldList(wordles, length)

    with open(filename, "w") as f:
        for word in word_list:
            f.write(word + "\n")

    print(f"Generated {len(word_list)} words and saved them to {filename}")

def save_acceptable_words(acceptable_words, filename="guessable.txt"):
    """ Save a list of acceptable words to a file, one word per line. """
    with open(filename, "w") as f:
        for word in acceptable_words:
            f.write(word + "\n")

    print(f"Saved {len(acceptable_words)} words to {filename}")

# Example list of words
wordles = WORDLES
acceptableWords = WORDS + WORDLES

# Run the function to generate and save words
#save_word_list_to_file(wordles)
save_acceptable_words(acceptableWords)