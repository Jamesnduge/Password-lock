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

    def setUp2(self):
        '''
        method to run before each test cases of Credentials.
        '''
        self.new_account = Credentials("Twitter", "darknight", "unlock")

    def test_init2(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.user_name,"darknight")
        self.assertEqual(self.new_account.key,"unlock")


    def test_delete_account(self):
        '''
        method to check if we can delete Credentials objects.
        '''
        self.new_account.save_account()
        test_account = Credentials("Twitter", "darknight", "unlock")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(user.accounts_list),1)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Credentials.display_accounts(),Credentials.accounts_list)

if __name__ == '__main__':
    unittest.main()
