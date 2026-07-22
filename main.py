from brain.llm import ask_llm
from brain.history import (
    get_messages,
    add_user,
    add_assistant
)

print("ROSE Assistant Started!\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        break

    add_user(user)

    answer = ask_llm(get_messages())

    print(f"ROSE : {answer}")

    add_assistant(answer)