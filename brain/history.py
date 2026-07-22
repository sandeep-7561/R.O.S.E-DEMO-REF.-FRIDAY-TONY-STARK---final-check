from brain.prompt import SYSTEM_PROMPT

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def get_messages():
    return messages


def add_user(message):
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant(message):
    messages.append(
        {
            "role": "assistant",
            "content": message
        }
    )