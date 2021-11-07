#ASCII Conversion Program

import time, sys

def banner():
    print(" ")
    time.sleep(1)
    print("Welcome to my ecryption program")
    time.sleep(1)
    print("The program uses a Caesar Cypher")
    print(" ")
    menu()

def menu():
    choice = input("Choose E to encrypt, D to decrypt or Q to quit ")
    if choice == "E" or choice == "e":
        encrypt()
    elif choice == "D" or choice == "d":
        decrypt()
    elif choice == "Q" or choice == "q":
        sys.exit()
    else:
        menu()

def encrypt():
    plaintext = input("Insert your plain text here ")
    print (" ")
    asciitext = [ord(c) for c in plaintext]
    print(asciitext)
    n = len(asciitext)
    cipherascii = []
    z = int(input("Select an encryption value for 1-10 "))
    print(" ")
    for i in range(0,n):
        x = asciitext[i] + z
        cipherascii.append(x)
    print(cipherascii)
    ciphertext = [chr(ascii) for ascii in cipherascii]
    time.sleep(2)
    print("The encrypted text is " + "".join(ciphertext))
    print(" ")
    menu()

def decrypt():
    plaintext = input("Insert your encrypted text here ")
    print(" ")
    asciitext = [ord(c) for c in plaintext]
    print(asciitext)
    n = len(asciitext)
    cipherascii = []
    z = int(input("Select an encryption value for 1-10 "))
    print(" ")
    for i in range(0,n):
        x = asciitext[i] - z
        cipherascii.append(x)
    print(cipherascii)
    ciphertext = [chr(ascii) for ascii in cipherascii]
    time.sleep(2)
    print("The decrypted text is " + "".join(ciphertext))
    print(" ")
    menu()
    
    
banner()

