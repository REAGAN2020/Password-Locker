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

    def tearDown(self):
        '''
            tear Down cleans up after each method has run
        '''
        User.user_list = []

    def test_save_multiple_users(self):
        '''
        test_save is basically to check if we can save multiple users into our user list
        '''
        self.new_user.save_user()
        test_user = User("facebook", "reagan", "pasword123", "reagan@gmail.com")  #new account
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
    def test_delete_user(self):
        '''
        test_delete is testing if we can delete our user from our user list
        '''
        self.new_user.save_user()
        test_user = User("facebook", "reagan", "pasword123", "reagan@gmail.com")
        test_user.save_user()
        #======deleting function=======
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        
    def test_find_user_by_user_name(self):
        '''
        test find user by name, checking if we can  find user by name and display info
        '''
        self.new_user.save_user()
        test_user = User("facebook", "reagan", "pasword123", "reagan@gmail.com")
        test_user.save_user()
        
        #=======finding user=========
        get_user = User.find_by_name("facebook")
        self.assertEqual(get_user.email,test_user.email)


    def test_user_exist(self):
        '''
        testing if account fu








if __name__ == '__main__':
    unittest.main()
