import hangman_template
import unittest
from collections import namedtuple
from string import ascii_lowercase

Test = namedtuple("Test", "input output")

__unittest = True


class TestHangman(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    longMessage = False

    def test_load_words(self):
        """Test loading wordlist
        """
        words = hangman_template.load_words()
        self.assertEqual(len(words), 55900)

    def test_is_word_guessed(self):
        secret_word = "queen"
        tests = [
            Test(["q"], True),
            Test(["q", "u"], False),
            Test(["q", "u", "e"], False),
            Test(["q", "r", "v"], False),
            Test([], False),
            Test([""], False),
            Test(["q", "u", "e", "n"], True),
            Test(["q", "u", "r", "n", "e", "w", "z", "q"], True),
        ]
        for test in tests:
            with self.subTest(test=test):
                is_guessed = hangman_template.is_word_guessed("queen", test.input)
                self.assertEqual(is_guessed, test.output)

    def test_get_available_letters(self):
        tests = [
            Test(ascii_lowercase[:i], ascii_lowercase[i:])
            for i in range(0, len(ascii_lowercase))
        ]
        tests.append(Test(ascii_lowercase, ""))
        for test in tests:
            self.assertEqual(hangman_template.get_remaining_letters(test.input), test.output)

    def test_get_guessed_word(self):
        secret_word = "queen"
        tests = [
            Test(["q"], "q_ _ _ _ "),
            Test(["q", "u"], "qu_ _ _ "),
            Test(["q", "u", "e"], "quee_ "),
            Test(["q", "r", "v"], "q_ _ _ _ "),
            Test([], "_ _ _ _ _ "),
            Test([""], "_ _ _ _ _ "),
            Test(["q", "u", "e", "n"], "queen"),
            Test(["q", "u", "r", "n", "e", "w", "z", "q"], "queen"),
        ]

        for test in tests:
            with self.subTest(test=test):
                guessed_word = hangman_template.get_guessed_word("queen", test.input)
                self.assertEqual(guessed_word, test.output)


if __name__ == "__main__":
    unittest.main(verbosity=0, buffer=True)
