import LSB
import Encryption_Layer
import pyfiglet


class Casper:

    def options(self):
        print(" Choose what to be done :-")
        print(" -------------------------\n")
        user_input = int(input(" 1. Encrypt\n"
                               " 2. Decrypt\n"
                               " 3. Generate keys\n"
                               " 4. Close program\n\n"))

        default = "\n Invalid Operation\n\n"

        return getattr(self, 'case_' + str(user_input), lambda: print(default))()

    def case_1(self):
        src = input(" Enter image name (with PNG extension):")
        message = input(" Enter data to be encoded: ")
        destination = input(" Enter the name of the new image (with PNG extension): ")
        encryption_key_file = input(" Specify the path of the encryption key: ")

        with open(encryption_key_file, "rb") as file:
            encryption_key = file.readline()

        Encryption_Layer.encrypt_message(src, message, destination, encryption_key)

    def case_2(self):
        hide_object = input(" Enter the hide object name (with PNG extension):")
        decryption_key_file = input(" Specify the path of the decryption key: ")

        with open(decryption_key_file, "rb") as file:
            decryption_key = file.readline()

        LSB.lsb_decode(hide_object, decryption_key)

    def case_3(self):
        Encryption_Layer.key_generator()

    def case_4(self):
        print(pyfiglet.figlet_format("Terminate the program", font="5lineoblique"))
        exit()
