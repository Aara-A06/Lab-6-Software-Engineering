# Encoder/Decoder Program
# My Name: Aara Ahn
# Partner's name: Kevin Zhang

def encode(password):
    """
    Encodes the 8-digit password by shifting each digit up by 3.
    """
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def decode(encoded_password):
    """
    Decodes the encoded password by shifting each digit down by 3.
    """
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password


def main():
    encoded_password = ""

    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if not encoded_password:
                print("No password has been encoded yet!")
            else:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif option == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

#This was really fun!
if __name__ == "__main__":
    main()
