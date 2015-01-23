__author__ = 'user'

import unittest
import hangman

class HangmanTestCase(unittest.TestCase):

    #checkCorrectAnswer(correctLetters, secretWord)
    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)


if __name__=="__main__":
 unittest.main()