import elgamal


def print_menu():
    print("Press 1 to generate the keys")
    print("Press 2 to encrypt a message")
    print("Press 3 to decrypt a message")
    print("Press 0 to exit")


def main():
    val = -1
    prkey = elgamal.PrivateKey(0, 0)
    pukey = elgamal.PublicKey(0, 0)
    while val != 0:
        print_menu()
        val = int(input("Enter your choice "))
        if val == 1:
           aux = generate_keys()
           prkey = aux['privateKey']
           pukey = aux['publicKey']
           print(pukey.p, prkey.p, "\n")
        elif val == 2:
            encrypt(pukey)
        elif val == 3:
           decrypt(prkey)
        else:
            pass


def generate_keys():
    n = 0
    c = 0
    n = int(input(" give N: "))
    c = int(input(" give C: "))
    return elgamal.generate_keys(n, c)


def verify(string):
    for char in string:
        if not (char.isalpha() or char == ' '):
            return False
    return True


def encrypt(pukey: elgamal.PublicKey):
    ok = False
    string = ""
    while not ok:
        string = input("Give the text to encrypt ")
        ok = verify(string)
        if not ok:
            print("Invalid Input! please use only letters and spaces")
    string = string.lower()
    res = elgamal.encrypt(pukey, string)
    print(res)


def decrypt(prkey: elgamal.PrivateKey):
    string = input("Give the text to decrypt ")
    res = elgamal.decrypt(prkey, string)
    print(res)


main()
