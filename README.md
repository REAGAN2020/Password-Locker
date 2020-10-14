<!-- # Password Locker

## Built By [Owiti Reagan](https://github.com/REAGAN2020/)

## Description
This application is used to store users online account credentials like account user names, email and passwords. Be warned that each session is stored in the RAM. So as soon as the application is closed, all data stored is lost.

## User Stories
These are the behaviours that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display guides for navigation | **In terminal: $./run.py** | Hello Welcome to your Pass Word Locker. What is your name? (once you enter your nname):Use these known short codes to operate : SU -> SIGN UP.  DA -> Display your account.  LN ->LOGIN.  ex ->exit Pass Word Locker. |
| Display prompt for creating an account | **Enter: su** | Enter account name, user name password and email .|
| Display prompt for login in | **Enter: ln** | Enter your account password to login |
| Once logged in | **You are now logged in to your  account** |  Use these short codes:CA -> Create new credential.DC -> Display your credentials list.  ex ->Log out your credentials account. |
| Display prompt for creating a credential | **Enter: ca** | Create new credential, Credential name: and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Log out account  | **Enter: ex** | You have logged out your  account |

* To completely interact with this application,you will need to sign up to have an account,then login to your account and work in there.

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* Good internet connection
*  For windows users:  GitBash
* For linux/ubuntu users : Git


### Cloning
* In your terminal:
        
        $ git clone https://github.com/REAGAN2020/Password-Locker.git
        $ cd Python-Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ ./main.py
      
        
## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ python3.8 credentials_test.py
        
## Technologies Used
* Python3.8

## License
[MIT](LICENSE.md) © @OwitiReagan -->
