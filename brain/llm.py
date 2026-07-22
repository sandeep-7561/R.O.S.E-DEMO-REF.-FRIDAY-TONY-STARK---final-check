from openai import OpenAI

from brain.prompt import SYSTEM_PROMPT

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


def ask_llm(messages):

    response = client.chat.completions.create(
        model="qwen3:4b",
        messages=messages,
        stream=False
    )

    return response.choices[0].message.content