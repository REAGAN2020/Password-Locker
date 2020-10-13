import unittest
from user import User


class TestAccount(unittest.TestCase):
    def setUp(self):

       self.new_user = User("facebook","reagan","password123","reagan@gmail.com")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.acc_name, "facebook")
        self.assertEqual(self.new_user.user_name, "reagan")
        self.assertEqual(self.new_user.password, "password123")
        self.assertEqual(self.new_user.email, "reagan@gmail.com")

    def test_save_user(self):
        '''
        test_save_user testing if the user is saved into the user list
        '''
        self.new_user.save_user()  
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
