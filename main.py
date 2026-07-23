import asyncio

from dotenv import load_dotenv

from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
    AutoSubscribe,
)

from livekit.plugins import openai, deepgram, silero

from brain.prompt import SYSTEM_PROMPT

load_dotenv()


class RoseAgent(Agent):

    def __init__(self):

        super().__init__(
            instructions=SYSTEM_PROMPT
        )


async def entrypoint(ctx: JobContext):

    await ctx.connect(
        auto_subscribe=AutoSubscribe.AUDIO_ONLY
    )

    session = AgentSession(

        vad=silero.VAD.load(),

        stt=deepgram.STT(),

        llm=openai.LLM.with_ollama(

            model="qwen3:4b",

            base_url="http://localhost:11434/v1",

        ),

        tts=openai.TTS(),
    )

    await session.start(

        room=ctx.room,

        agent=RoseAgent(),
    )

    print("ROSE Started...")

    await session.generate_reply(

        instructions="Introduce yourself."
    )

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":

    cli.run_app(

        WorkerOptions(

            entrypoint_fnc=entrypoint

        )

    )