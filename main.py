import CASPER
import pyfiglet


# Main function
def main():

    print(pyfiglet.figlet_format("CASPER\n", font="slant"))
    print(pyfiglet.figlet_format(" CASPER ready for action\n", font="digital"))

    casper = CASPER.Casper()

    while True:
        casper.options()


# Driver Code
if __name__ == "__main__":
    main()
