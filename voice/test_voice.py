from speech_to_text import listen

while True:

    text = listen()

    print()

    print("You Said :", text)

    print()

    if text.lower() == "exit":

        break