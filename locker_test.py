import unittest
from passwordLocker import User, Credentials

class TestLocker(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
        '''
        tearDown method to clean up after each test case has run.
        '''
        User.users_list = []

    def save_user(self):
        User.users_list.append(self)

    def setUp(self):
        '''
        method to run before each test cases.
        '''
        self.new_user = User("Jamesnduge", "tj193345")

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Jamesnduge")
        self.assertEqual(self.new_user.password,"tj193345")

    def test_save_user(self):
        '''
        test case to test if the user object is saved into
         the users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_users(self):
        '''
        test case to check if we can save multiple user
        objects to our users_list
        '''
        self.new_user.save_user()
        test_user = User("Test","unlock")
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_display_all_users(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(User.display_users(),User.users_list)


    def tearDown2(self):
        '''
        tearDown method to clean up after each test case has run.
        '''
        Credentials.accounts_list = []

    def setUp2(self):
        '''
        method to run before each test cases of Credentials.
        '''
        self.new_account = Credentials("Twitter", "darknight", "unlock")

    def test_init2(self):
        '''
        test case to test if the object is initialized properly
        '''
        self.new_account = Credentials("Twitter", "darknight", "unlock")

        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.user_name,"darknight")
        self.assertEqual(self.new_account.key,"unlock")


    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Credentials.display_accounts(),Credentials.accounts_list)

    def test_generate_password(self):
        '''
        method that returns a list of all accounts saved
        '''
        self.twitter = Credentials('Twitter','maryjoe','')
        self.twitter.password = Credentials.generate_password(8)
        self.assertEqual(len(Credentials.generate_password(8)),8)





if __name__ == '__main__':
    unittest.main()
