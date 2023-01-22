import codecs
import LSB
import Encryption_Layer


def obfuscate(src, message, destination):
    obfuscate_message = codecs.encode(message, 'rot13')
    LSB.lsb_encode(src, obfuscate_message, destination)


def reverse_obfuscate(src, decrypted_key):
    Encryption_Layer.decrypt_message(codecs.decode(src, 'rot13'), decrypted_key)
