def encrypt(inputText, N, D):
    reverseString = inputText[::-1]  # string reversal
    stringArr = []
    stringArr[:] = reverseString
    modifiedArr = []
    if D == 1:
        for letter in stringArr:
            if (letter != "!") and (letter != " "):
                modifiedArr.append(chr(ord(letter) + N))
            else:
                modifiedArr.append(letter)
        return "".join(modifiedArr)
    elif D == -1:
        for letter in stringArr:
            if (letter != "!") and (letter != " "):
                modifiedArr.append(chr(ord(letter) - N))
            else:
                modifiedArr.append(letter)
        return "".join(modifiedArr)


def decrypt(encryptedText, N, D):
    stringArr = []
    stringArr[:] = encryptedText
    modifiedArr = []
    if D == 1:
        for letter in stringArr:
            if (letter != "!") and (letter != " ") and (letter != "\n"):
                modifiedArr.append(chr(ord(letter) - N))
            else:
                modifiedArr.append(letter)
        decryptedStr = "".join(modifiedArr)
        decryptedStr = decryptedStr[::-1]
        return decryptedStr
    elif D == -1:
        for letter in stringArr:
            if (letter != "!") and (letter != " ") and (letter != "\n"):
                modifiedArr.append(chr(ord(letter) + N))
            else:
                modifiedArr.append(letter)
        decryptedStr = "".join(modifiedArr)
        decryptedStr = decryptedStr[::-1]
        return decryptedStr
