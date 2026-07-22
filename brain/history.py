"""
ROSE Conversation History
Stores the current chat session.
"""

from brain.prompt import SYSTEM_PROMPT


# Conversation History
conversation_history = [

    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }

]


def get_history():
    """
    Return complete conversation history.
    """
    return conversation_history


def add_user_message(message: str):
    """
    Save user's message.
    """
    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant_message(message: str):
    """
    Save assistant response.
    """
    conversation_history.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def clear_history():
    """
    Reset conversation.
    """

    conversation_history.clear()

    conversation_history.append(
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    )