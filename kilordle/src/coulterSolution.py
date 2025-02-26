from words import WORDS, WORDLES

class WordScorer:
    def __init__(self):
        self.firstPos = []
        self.secondPos = []
        self.thirdPos = []
        self.fourthPos = []
        self.fifthPos = []

        self.score5 = []
        self.score4 = []
        self.score3 = []
        self.score2 = []
        self.score1 = []
        self.score0 = []

    def getWordScore(self, word):
        score = 0
        for i, char in enumerate(word):
            if i == 0 and char not in self.firstPos:
                score += 1
            elif i == 1 and char not in self.secondPos:
                score += 1
            elif i == 2 and char not in self.thirdPos:
                score += 1
            elif i == 3 and char not in self.fourthPos:
                score += 1
            elif i == 4 and char not in self.fifthPos:
                score += 1
        return score
    
    def getAllWordsWithScore(self, words, score):
        if score >= 0 and score <= 5:

            if score == 5:
                for word in words:
                    if self.getWordScore(word) == 5:
                        self.score5.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

            elif score == 4:
                for word in words:
                    if self.getWordScore(word) == 4:
                        self.score4.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

            elif score == 3:
                for word in words:
                    if self.getWordScore(word) == 3:
                        self.score3.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

            elif score == 2:
                for word in words:
                    if self.getWordScore(word) == 2:
                        self.score2.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

            elif score == 1:
                for word in words:
                    if self.getWordScore(word) == 1:
                        self.score1.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

            elif score == 0:
                for word in words:
                    if self.getWordScore(word) == 0:
                        self.score0.append(word)
                        self.firstPos.append(word[0])
                        self.secondPos.append(word[1])
                        self.thirdPos.append(word[2])
                        self.fourthPos.append(word[3])
                        self.fifthPos.append(word[4])

        else:
            print("Invalid score. Please enter a score between 0 and 5.")
            return
    
def main():
    totalWords = WORDS + WORDLES
    scorer = WordScorer()
    scorer.getAllWordsWithScore(totalWords, 5)
    scorer.getAllWordsWithScore(totalWords, 4)
    scorer.getAllWordsWithScore(totalWords, 3)
    scorer.getAllWordsWithScore(totalWords, 2)
    scorer.getAllWordsWithScore(totalWords, 1)
    scorer.getAllWordsWithScore(totalWords, 0)

    print("Words with score 5:", scorer.score5)
    print("Words with score 4:", scorer.score4)
    print("Words with score 3:", scorer.score3)
    print("Words with score 2:", scorer.score2)
    print("Words with score 1:", scorer.score1)
    print("Words with score 0:", scorer.score0)

if __name__ == "__main__":
    main()