import re


class Palindrome:
    # palindrome initializer method
    def __init__(self, candidate):
        # input values
        self._candidate = candidate  # input string
        self._length = len(candidate)  # input length
        # analysis values
        self._is_a_palindrome = False  # initialize status
        self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
        self._analysis = []  # array of tests
        self._tests = 0  # counter of tests performed
        # evaluate for palindrome
        self.is_palindrome()

    # palindrome tester method
    def is_palindrome(self):
        c = self._az09
        # Run loop from 0 to len/2 of string (middle is exit point)
        tests = int(len(c) / 2)
        for i in range(0, tests):
            front = c[i];
            back = c[len(c) - i - 1]
            if front.lower() == back.lower():
                self.logger(front, back, True)
                self._tests += 1
            else:
                self.logger(front, back, False)
                return
        self._is_a_palindrome = True
        return

    # palindrome logging
    def logger(self, front, back, result):
        self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

    # getters follow
    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self._is_a_palindrome

    @property
    def analysis(self):
        return self._analysis

def word():
    word1 = input("What word would you like to test?")
    palin = Palindrome(word1)
    print(f"Is the word a palindrome?{word1} = {palin._is_a_palindrome}")

if __name__ == "__main__":
    word()

    n = "row"
    a = "epic"
    t = "racecar"
    h = "anna"
    k = "start"
    p = "yay"
    l = "salutations"
    o = "yummy"
    j = "jumping"
    i = "banana"

    palindrome = Palindrome(n)
    palindrome1 = Palindrome(a)
    palindrome2 = Palindrome(t)
    palindrome3 = Palindrome(h)
    palindrome4 = Palindrome(k)
    palindrome5 = Palindrome(p)
    palindrome6 = Palindrome(l)
    palindrome7 = Palindrome(o)
    palindrome8 = Palindrome(j)
    palindrome9 = Palindrome(i)

    print(f"Is the word a palindrome? {n} = {palindrome._is_a_palindrome}")
    print(f"Is the word a palindrome? {a} = {palindrome1._is_a_palindrome}")
    print(f"Is the word a palindrome? {t} = {palindrome2._is_a_palindrome}")
    print(f"Is the word a palindrome? {h} = {palindrome3._is_a_palindrome}")
    print(f"Is the word a palindrome? {k} = {palindrome4._is_a_palindrome}")
    print(f"Is the word a palindrome? {p} = {palindrome5._is_a_palindrome}")
    print(f"Is the word a palindrome? {l} = {palindrome6._is_a_palindrome}")
    print(f"Is the word a palindrome? {o} = {palindrome7._is_a_palindrome}")
    print(f"Is the word a palindrome? {j} = {palindrome8._is_a_palindrome}")
    print(f"Is the word a palindrome? {i} = {palindrome9._is_a_palindrome}")
