import asyncio
from message import get_inference_server_reply
from helpers import get_system_prompt
from settings import Models

async def main():
    system_prompt = get_system_prompt()
    await get_inference_server_reply(system_prompt=system_prompt, model="Goliath120b", msg="are you my dirty little cumslut?")
    
    print("\nDone")

asyncio.run(main())