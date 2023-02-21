# This is a sample Python script.
import cipher


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def encrypt(inputText, N, D): #task 1
    # Use a breakpoint in the code line below to debug your script.
    newText = ""
    i = len(inputText)-1
    while i > -1:
        newText= newText + inputText[i]
        i = i-1
    #replace ASCII
    retText = ""
    for c in newText:
        if D > 0:
            c = chr((ord(c)) + N)
        else:
            c = chr((ord(c)) - N)
        retText = retText + str(c)
    return retText


def decrypt(inputText, N, D): # task2
    # Use a breakpoint in the code line below to debug your script.
    newText = ""
    i = len(inputText) - 1
    while i > -1:
        newText= newText + inputText[i]
        i = i-1
    #replace ASCII
    retText = ""
    for c in newText:
        if D > 0:
            c = chr((ord(c)) - N)
        else:
            c = chr((ord(c)) + N)
        retText = retText + str(c)
    return retText

def decryptFile( filename): # code that opens file and decrpts it returns array of decrypted userid and password
    r = []
    f = open(filename,"r")
    lines = f.readlines()
    i = 0
    for line in lines:
       r[i] =  decrypt(lines, 1,3)
       i+=1
    return r
#asamant and aisha meet it
#bjha and skharel have passwords that dont match
#ALLy! does not meet ht erequirement
