from openai import OpenAI
from brain.prompt import SYSTEM_PROMPT

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


