import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def fileKey():
    key = Fernet.generate_key()
    print(" ")
    print("Key = ", key)
    print(" ")
    fileName = input("Enter a filename for Symmetric Key: ")
    fileName = fileName + ".key"
    print(" ")
    print("Creating File: ", fileName)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    print(" ")
    file = open(fileName, 'wb')  # wb = write bytes
    file.write(key)
    file.close()
    return

def keyPairs():
    print(" ")
    fileName = input("Enter a name for the pair(no extensions): ")
    print(" ")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    fileName1 = fileName + "_private_key.pem"
    with open(fileName1, 'wb') as f:
        f.write(pem)

    pem2 = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    fileName2 = fileName + "_public_key.pem"
    with open(fileName2, 'wb') as f2:
        f2.write(pem2)

    f.close()
    f2.close()
    print(" ")
    print(f"Creating files {fileName1} and {fileName2}")
    print(" ")
    return

def cryptFile():
    print(" ")
    fileName = input("Enter a file to Encrypt(with extension): ")
    print(" ")
    keyName = input("Select a file with a symmetric key to use for Encryption: ")
    file = open(fileName, "rb")
    message = file.read()
    file.close()

    file2 = open(keyName, 'rb')
    key = file2.read()
    file2.close()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(message)

    fileName2 =  fileName + ".secret.file"
    print(" ")
    print(f"Creating {fileName2}")
    print(" ")
    file3 = open(fileName2, "wb")
    file3.write(encrypted)
    file3.close()
    return

def cryptPass():
    print(" ")
    pubFile = input("Enter name of Public Key file to use: ")
    print(" ")
    keyFile = input("Enter name of symmetric key file to encrypt: ")
    print(" ")

    with open(pubFile, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    with open(keyFile, "rb") as sym_file:
        message = sym_file.read()

    print(message)
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(encrypted)

    print(" ")
    outFile = input("Enter name for encrypted passkey file(no extension): ")
    print(" ")
    outFile = outFile + ".secret.pass"
    file1 = open(outFile, "wb")
    file1.write(encrypted)
    file1.close()
    return

def dCryptKey():
    print(" ")
    privFile = input("Enter name of Private Key file to use: ")
    print(" ")
    keyFile = input("Enter name of symmetric key file to decrypt: ")
    print(" ")


    with open(privFile, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    file = open(keyFile, "rb")
    encrypted = file.read()
    file.close()

    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(original_message.decode())

    outFile = keyFile[:-12] + ".key"
    file2 = open(outFile, "wb")
    file2.write(original_message)
    file2.close()
    print(" ")
    print(f"Creating File: {outFile}")
    print(" ")

def dCryptFile():
    print(" ")
    keyFile = input("Enter name of Symmetric Key file to use: ")
    print(" ")
    secretFile= input("Enter name of encrypted file to decrypt: ")
    print(" ")

    file = open(secretFile, "rb")
    message = file.read()
    file.close()

    file2 = open(keyFile, 'rb')
    key = file2.read()
    file2.close()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(message)

    outFile = secretFile[:-12]
    file3 = open(outFile, "wb")
    file3.write(decrypted)
    file3.close()
    print(" ")
    print(f"Creating File {outFile}")
    print(" ")




def main():
    quitter = " "
    while quitter != "Q":
        print("**************** Encryption Program ******************")
        print(" ")
        print("Create Symmetric Key:                  A")
        print("Create Asymmetric Key pair:            B")
        print("Encrypt File Symmetrically:            C")
        print("Encrypt Symmetric Key with Public Key: D")
        print("Decrypt Symmetric Key:                 E")
        print("Decrypt File Symmetrically:            F")
        print("To Quit:                               Q")
        quitter = input("Make A Selection: ").upper()
        match quitter:
            case "A":
                fileKey()
            case "B":
                keyPairs()
            case "C":
                cryptFile()
            case "D":
                cryptPass()
            case "E":
                dCryptKey()
            case "F":
                dCryptFile()
            case "Q":
                print(" ")
                print("************** Cya Later! ****************")
                break
            case _:
                print("Invalid Input, Try again!")

if __name__ == '__main__':
    main()