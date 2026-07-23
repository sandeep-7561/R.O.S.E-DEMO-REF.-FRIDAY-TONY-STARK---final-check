import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext,WorkerOptions,cli,llm
from livekit.agents.voice_assistant import VoiceAssistant

load_dotenv()

from livekit.plugins import openai, silero

llm = openai.LLM.with_ollama(
    model="qwen3:4b",
    base_url="http://localhost:11434/v1"
)

async def enterypoint(ctx: JobContext)