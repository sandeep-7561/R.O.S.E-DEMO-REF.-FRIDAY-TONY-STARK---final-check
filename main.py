import re

from brain.llm import ask_llm
from brain.history import (
    get_messages,
    add_user,
    add_assistant
)

from memory.database import (
    save_memory,
    get_memory
)

print("ROSE Assistant Started!\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        break

    # ---------- MEMORY SAVE ----------

    match = re.search(
        r"my name is (.+)",
        user,
        re.IGNORECASE
    )

    if match:

        name = match.group(1).strip()

        save_memory("name", name)

    # ---------- MEMORY READ ----------

    if user.lower() == "what is my name?":

        name = get_memory("name")

        if name:

            print(f"ROSE : Your name is {name}")

            continue

    add_user(user)

    answer = ask_llm(get_messages())

    print(f"ROSE : {answer}")

    add_assistant(answer)