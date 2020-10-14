from user import User
from social import Credentials


def create_user(acc_name, user_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = User(acc_name, user_name, password, email)
    return new_user


def save_user(user):
    '''
    Function to save account
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)


def check_existing_user(name):
    '''
    Function that check if an user exists with that name and return a Boolean
    '''
    return User.user_exist(name)


def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def create_credentials( user_name, password, email):
    '''
    Function to create a new user
    '''
    new_credentials = Credentials(user_name, password, email)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save user
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a user by nane and returns the user
    '''
    return Credentials.find_by_name(name)


def check_existing_credentials(name):
    '''
    Function that check if an user exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_credentials()


def main():
    print("Hello welcome to password locker.What is your name")
    user_name = input()
    print(
        f"Hello {user_name}, sign up to Password Locker to create an account.")
    print('\n')
    while True:
        print("To continue please select one of these short codes :\n su for Sign Up.\n da for display your account.\n ln for login.\n ex for exit. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create an  Account")
            print("_"*100)
            acc_name = input('Account name:')
            print('\n')
            user_name = input('User name:')
            print('\n')
            pwd = input('Password : ')
            print('\n')
            e_address = input('Email address:')
            save_user(create_user(acc_name, user_name, pwd, e_address))
            print('\n')
            print(
                f"A New {acc_name} Account with the user name  {user_name} has been created.")
            print(
                f"You can now login to your {acc_name} account using your password.")
            print('\n')
        elif short_code == 'da':
            if display_user():
                print("Thank you for signing up. here are your login credentials")
                print('\n')
                for user in display_user():
                     print(
                         f"User name:{user.acc_name}  User name: {user.user_name} Password:{user.password}")
                     print('\n')
            else:
                print('\n')
                print(
                     "You dont seem to have created an account.Sign up to create a new account.")
                print('\n')
        elif short_code == 'ln':
            print("Enter your password to login.")
            search_user = input()
            if check_existing_user(search_user):
                find_credentials = find_user(find_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {user_name} account")
                print("\033[1;37;1m   \n")
                #========================================CREDENTIALS AREA=======================================================================
                while True:
                    print('''
                    Use these short codes:
                    ca -> Create new credential.
                    dc -> Display your credentials list
                    ex ->Log out your credentials account.''')
                    short_code = input().lower()
                    if short_code == "ca":
                        print("Create new credential")
                        print('_' * 20)
                        credentials_name = input('Credential name:')
                        print('\n')
                        user_name = input(f"{credentials_name} user name:")
                        print('\n')
                        print('*' * 20)
                        password = input(f"{credentials_name} password:")
                        save_credentials(create_credentials(user_name, password, email))
                           
                        print('\n')
                        print(
                            f"A New {credentials_name} Account with the user name  {user_name} has been created.")
                        print('\n')
                    elif short_code == 'dc':
                        if display_credentials():
                             print("Here are your credentials details")
                             print('\n')
                             for credentials in display_credentials():
                                 print(
                                     f"Credential name:{credentials.credentials_name}  User name: {credentials.usr_name} Password:{credentials.password}")
                                 print('\n')
                        else:
                            print('\n')
                            print(
                                "You do not have any account saved at the moment")
                            print('\n')
                    elif short_code == "ex":
                        print('\n')
                        print(
                            f"You have logged out your {user_name} account")
                        print("Bye see you some other time")
                        print('\n')
                        break

            else:
                print('\n')
                print("invalid password!! please try again")
                print('\n')
                print('\n')

        elif short_code == "ex":
                print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                break
                
        else:
                   print("please use short codes to continue")


if __name__ == '__main__':
    main()
