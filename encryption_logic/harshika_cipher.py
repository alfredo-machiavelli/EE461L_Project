
# TASK 1
def encrypt(original_string, N, D):

    #resulting string
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

# TASK 2
def decrypt(encrypted_string, N, D):
    # resulting string
    result = ""

    # we are going to loop through each char in the string
    # for every character in inputText
    # [::-1] means start at the end of the string + move back by 1 [hence the -1]
    for character in encrypted_string[::-1]:

        # since space and ! are not encrypted
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

