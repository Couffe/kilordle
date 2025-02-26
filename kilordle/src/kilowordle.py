import time

def seedRandom(numWordles):
    pstNow = time.time() - 2880
    return pstNow // 86400

def genWorldList(wordles, length = 1000):
    
    numWordles = len(wordles)
    
    wordList = []
    generator = 163
    random = seedRandom(numWordles)
    
    for i in range(length):
        wordList.append(wordles[int((random + generator * i) % numWordles)])
        
    return wordList
    
class wordle:
    def __init__(self, word):
        self.word = word
        self.correct = [False] * len(word)
        self.clues = []
        self.solved = False
        self.score = 0
            
    def __str__(self):
        if len(self.clues) <= 0:
            return ''.join(self.correct)
        else:
            return self.clues[len(self.clues) - 1]
            
    def guess(self, word):
        # setup clue buffer
        clue = [0] * len(self.word)
        
        # loop the guess, fill out correct list and clues
        for i in range(len(word)):
            if i >= len(self.word):
                break
                
            letter = word[i]
                
            if letter == self.word[i]:
                clue[i] = 2
                self.correct[i] = True
            else:
                totalMisplaced = 0
                previousMisplaced = 0
                for j in range(len(self.word)):
                    if self.word[j] == letter and word[j] != letter:
                        totalMisplaced += 1
                                
                for j in range(i):
                    if word[j] == letter and self.word[j] != letter:
                        previousMisplaced += 1
                        
                clue[i] = 1 if previousMisplaced < totalMisplaced else 0
        
        # save clue to the clue history
        self.clues.append(clue)
        
        # solved if correct is all true
        self.solved = all(self.correct)
        
        # calculate score sort value
        correctMask = 0
        misplacedMask = 0
        self.score = 0
        for i in range(min(5, len(self.clues))):
            clue = self.clues[len(self.clues) - i - 1]
            for j in range(len(clue)):
                code = clue[j]
                if code == 2 and (correctMask & (1 << j)) != (1 << j):
                    self.score += 25 # correct letter
                    correctMask |= 1 << j
                elif code == 1:
                    self.score += 1
        
    
class kilowordle:
    def __init__(self, wordles, words, length = 1000):
        self.wordSet = set(words)
        self.wordSet.update(wordles)
        self.wordles = []
        self.guesses = []
        self.solved = 0
        wordList = genWorldList(wordles)
        for word in wordList:
            self.wordles.append(wordle(word))
            
    def guess(self, word):
        word = word.lower()
        if len(word) != 5 or not word in self.wordSet:
            return False
            
        self.guesses.append(word)
        for wordle in self.wordles:
            if wordle.solved:
                continue
                
            wordle.guess(word)
            if wordle.solved:
                self.solved += 1
        return True
            
    def guessMany(self, words):
        for word in words:
            self.guess(word)
                
    def print(self, length = 12, columns = 4, debug = False):
        topBoards = sorted(
            [w for w in self.wordles if not w.solved],  # only boards not solved
            key=lambda w: -w.score  # sort by sort value
        )
        
        remaining = len(topBoards)
        length = min(length, remaining)
        del topBoards[length:]
        
        if remaining > length:
            print()
            print(f"+ {remaining - length} more...")
            print()
        
        for i in range(0, length, columns):
            if debug:
                # print debug word
                for k in range(columns):
                    wordleIndex = length - (i + k) - 1
                    if wordleIndex < 0:
                        break
                    if k != 0:
                        print('     ', end='')
                    wordle = topBoards[wordleIndex]
                    print('    ', end='')
                    print(wordle.word, end='')
                    print('    ', end='')
                print()
            
            # print header
            for k in range(columns):
                wordleIndex = length - (i + k) - 1
                if wordleIndex < 0:
                    break
                if k != 0:
                    print('     ', end='')
                print('_____________', end='')
            print()
            
            for j in range(6):
                offset = max(0, 5 - len(self.guesses))
                guessIndex = len(self.guesses) - 5 + j + offset
                guess = self.guesses[guessIndex] if guessIndex >= 0 and guessIndex < len(self.guesses) else None
                
                # print guess
                for k in range(columns):
                    wordleIndex = length - (i + k) - 1
                    if wordleIndex < 0:
                        break
                    if k != 0:
                        print('     ', end='')
                    print('[ ', end='')
                    if guess is None:
                        print('          ', end='')
                    else:
                        for letter in guess:
                            print(letter, end='')
                            print(' ', end='')
                    print(']', end='')
                                
                print()
                                    
                # print clue
                if guess is None:
                    print(end='')
                else:
                    for k in range(columns):
                        wordleIndex = length - (i + k) - 1
                        if wordleIndex < 0:
                            break
                        if k != 0:
                            print('     ', end='')
                        wordle = topBoards[wordleIndex]
                        clue = wordle.clues[guessIndex]
                        print('  ', end='')
                        for code in clue:
                            if code == 1:
                                print('~ ', end='')
                            elif code == 2:
                                print('# ', end='')
                            else:
                                print('  ', end='')
                        print(' ', end='')
                                                
                print()
            print()
