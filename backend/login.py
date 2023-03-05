from bson import ObjectId
from getpass import getpass
from pymongo import MongoClient
import pymongo


client = MongoClient("mongodb+srv://suprita:jungK00K@supritadb.m2chzrd.mongodb.net/?retryWrites=true&w=majority")
db = client.UserDB
collection = db.UserCollection0

# sample fieldst = {"Username": "suprita",
#         "First Name": "Suprita",
#         "Last Name": "Ashok",
#         "UserID": ObjectId(),
#         "Password": "password",
#         }


def encrypt(original_string, N, D):
    result = ""

    #we are going to loop through each char in the string
    #for every character in inputText
    #[::-1] means start at the end of the string + move back by 1 [hence the -1]

    for character in original_string[::-1]:

        # since space and ! are not encrypted
        if character == ' ' or character == '!':
            result = character + result


        else:

            #ord will return the ascii value of the char
            val = ord(character) + (N * D)

            # if the value is lower than 34, then we subtract the diff from 126
            if val < 34:
                val = 126 - (34 - val)

            #so if the value is higher than 126, then we add the diff to 34
            if val> 126:
                val = 34 + (val- 126)

            #chr is the letter associated with the ascii value
            #add this to the result
            result = chr(val) + result


    return result

def decrypt(encrypted_string, N, D):
    result = ""

    # we are going to loop through each char in the string
    # for every character in inputText
    # [::-1] means start at the end of the string + move back by 1 [hence the -1]
    for character in encrypted_string[::-1]:
        # characters space and ! are not encrypted
        if character == ' ' or character == '!':
            result = character + result
        else:
            val = ord(character) - N * D
            if val> 126:
                val = 34 + (val - 126)
            if val < 34:
                val = 126 - (34 - val)
            result = chr(val) + result

    return result

def signup():
    print("Welcome to the Hardware Library")

    firstName = input("What's your first name? ")
    while not firstName.isalnum():
        firstName= input("Make sure your first name doesn't have any numbers!\n What's your first name? ")

    lasttName = input("What's your last name? ")
    while not lasttName.isalnum():
        lasttName = input("Make sure your last name doesn't have any numbers!\n What's your lastname? ")

    username = input("Please select a username: @")
    while not username.isalnum():
        username = input("Make sure your username only contains numbers and letters!\n"
                         "Please select a username: @")

    # password = getpass("Please select a password: ")
    password = input("Please select a password: ")
    while not password.isalnum() :
        # password = getpass("Make sure your password is at least 5 characters long "
        #                  "and only contains numbers and letters!\n"
        #                    "Please select a password: ")
        password = input("Make sure your password is at least 5 characters long "
                           "and only contains numbers and letters!\n"
                           "Please select a password: ")

    newUser = {"Username": username,
            "First Name": firstName,
            "Last Name": lasttName,
            "UserID": ObjectId(),
            "Password": encrypt(password, 4, -1),
            }

    resource_id = collection.insert_one(newUser).inserted_id
    return

signup()
