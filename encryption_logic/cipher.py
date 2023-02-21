# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def encrypt(text, n, d):
    if d != -1 and d != 1 : return -1
    else:
        text = reverse(text)
        encrypted = ""
        for c in text:
            if ord(c) >= 34: encrypted += chr(ord(c) + (d * n))
            else: return "Text cannot have non-printable characters, spaces, or exclamation points"
        return encrypted

def decrypt(encryptedText, n, d):
    text = ""
    for c in encryptedText:
        if ord(c) >= 34: text += chr(ord(c) + (d * n * -1))
        else: return "Text cannot have non-printable characters, spaces, or exclamation points"
    text = reverse(text)
    return text

def reverse(text):
    revText = ""
    i = len(text) - 1
    while i >= 0:
        revText += text[i]
        i-=1
    return revText


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = 'a'
    print(test)
    print(chr(ord(test) + 4))

    print(reverse("hi my name is suprita"))
    print(reverse(reverse("hi my name is suprita")))
    t1 = "TEST"
    t2 = "hi my name is suprita"
    t3 = "racecar"

    print(encrypt(t1, 2, 1))
    t1 = encrypt(t1, 2, 1)
    print(decrypt(t1, 2, 1))
    t1 = decrypt(t1, 2, 1)

    print(encrypt(t1, 4, -1))
    t1 = encrypt(t1, 4, -1)
    print(decrypt(t1, 4, -1))
    t1 = decrypt(t1, 4, -1)

    print(encrypt(t2, 3, 1))
    t2 = encrypt(t2, 3, 1)
    print(decrypt(t2, 3, 1))
    t2 = decrypt(t2, 3, 1)

    print(encrypt(t3, 2, -1))
    t3 = encrypt(t3, 2, -1)
    print(decrypt(t3, 2, -1))
    t3 = decrypt(t3, 2, -1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
