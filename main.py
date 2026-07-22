from brain.llm import ask_llm


def main():

    print("ROSE Assistant Started!")
    print("Type 'exit' to quit.\n")

    while True:

        user_message = input("You : ")

        if user_message.lower() == "exit":
            print("ROSE : Goodbye")
            break

        response = ask_llm(user_message)

        print(f"ROSE : {response}")


if __name__ == "__main__":
    main()