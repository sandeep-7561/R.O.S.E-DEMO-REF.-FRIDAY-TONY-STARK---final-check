from openai import OpenAI

from brain.history import (
    get_history,
    add_user_message,
    add_assistant_message
)


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


def ask_llm(user_message: str):

    # Save user message
    add_user_message(user_message)

    response = client.chat.completions.create(

        model="qwen3:4b",

        messages=get_history(),

        temperature=0.2,

        max_tokens=500,

        reasoning_effort="none",

        stream=False
    )

    assistant_reply = response.choices[0].message.content

    # Save assistant response
    add_assistant_message(assistant_reply)

    return assistant_reply