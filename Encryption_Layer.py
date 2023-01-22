import Obfuscation_Layer
from cryptography.fernet import Fernet


def key_generator():
    key = Fernet.generate_key()
    key_file_name = input(" Enter the key file name: ")
    key_file_name = key_file_name + ".pubkey"
    key_file = open(key_file_name, "w")
    key_file.write(str(key).replace("b'", "").replace("'", ""))


def encrypt_message(src, message, destination, encryption_key):
    encryption_object = Fernet(encryption_key)
    encrypted_message = str(encryption_object.encrypt(bytes(message, 'utf-8')))\
        .replace("b'", "")\
        .replace("'", "")
    Obfuscation_Layer.obfuscate(src, encrypted_message, destination)


def decrypt_message(cipher_text, decrypt_key):
    decryption_object = Fernet(decrypt_key)
    decrypted_message = str(decryption_object.decrypt(cipher_text))\
        .replace("b'", "")\
        .replace("'", "")
    decrypted_message_file = open("Secret Message.txt", "w")
    decrypted_message_file.write(decrypted_message)
    print("\n Image decoded successfully\n")
