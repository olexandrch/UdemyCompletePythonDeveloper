#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 192. Unittest

import unittest
import Sec_15_192_Unittest

print(Sec_15_192_Unittest.do_stuff(5))
print(Sec_15_192_Unittest.do_stuff('saer'))
print(Sec_15_192_Unittest.do_stuff(0))
print(Sec_15_192_Unittest.do_stuff(None))
print('='*40)


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to start the test')

    def test_do_staff(self):
        '''Testing for correct adding'''
        test_param = 10
        result = Sec_15_192_Unittest.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_staff2(self):
        test_param = 'wer'
        result = Sec_15_192_Unittest.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_staff3(self):
        test_param = None
        result = Sec_15_192_Unittest.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_staff4(self):
        test_param = ''
        result = Sec_15_192_Unittest.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()

# run in terminal
# python -m unittest -v
