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
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Jamesnduge", "tj193345")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Jamesnduge")
        self.assertEqual(self.new_user.password,"tj193345")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    

if __name__ == '__main__':
    unittest.main()
