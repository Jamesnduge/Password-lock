import unittest
from passwordLocker import User

class TestLocker(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []

        def save_user(self):
            User.users_list.append(self)


if __name__ == '__main__':
    unittest.main()
