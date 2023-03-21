import sys
import json

from bson import ObjectId
from getpass import getpass
from bson.json_util import dumps
from pymongo import MongoClient
import pymongo


client = MongoClient("mongodb+srv://suprita:jungK00K@supritadb.m2chzrd.mongodb.net/?retryWrites=true&w=majority")
db = client.UserDB
users = db.UserCollection0

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

def login(inputUsername, inputPassword):
    username = inputUsername
    while users.find_one({"Username": username}) is None:
        username = input("Username not found. Please try again: ")
    thisUser =  users.find_one({"Username": username})
    correctPass = decrypt(str(thisUser["Password"]), 4, -1)
    password = inputPassword
    while password !=  correctPass:
        password = input("Incorrect password. Please try again: ")
    print("Login successful! Welcome " + thisUser["First Name"] + "!")
    return

def signup(fullName, username, password):
    nameArr = fullName.split()

    newUser = {"Username": username,
            "First Name": nameArr[0],
            "Last Name": nameArr[1],
            "Password": encrypt(password, 4, -1),
            }

    resource_id = users.insert_one(newUser).inserted_id
    print(fullName, 'has been added to the database.')

def main():
    print("Welcome to h/w library!")
    try:
        which =input("Would you login, signup, or exit the application?")
        if which == "login":
            login()
        elif which == "signup":
            signup()
        elif which == "exit":
            sys.exit()
    except KeyboardInterrupt: print("\nGood Bye!")


if __name__ == "__main__":
    main()