from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

print("LLM Test Started")
print("Type 'exit' to quit.\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = client.chat.completions.create(
        model="qwen3:4b",
        messages=messages,
        stream=False
    )

    answer = response.choices[0].message.content

    print(f"AI : {answer}")

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )