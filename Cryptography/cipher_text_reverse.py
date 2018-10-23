def main():
    plain_text_message = "This is my secret message"
    cipher_text = ""

    i = len(plain_text_message) - 1

    while i >= 0:
        cipher_text += plain_text_message[i]
        i -= 1

    print("The cipher text is: ", cipher_text)

main()
