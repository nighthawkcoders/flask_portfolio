import unittest


class MyTestCase(unittest.TestCase):
    def make_candy(small, big, goal):
        if goal >= 5 * big:
            rem = goal - 5 * big

        elif rem <= small:
            return rem

        return -1

    make_candy(4,1,9)



if __name__ == '__main__':
    unittest.main()
