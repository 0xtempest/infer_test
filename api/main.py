from api.message import get_inference_server_reply
from api.helpers import get_system_prompt

async def main():
    system_prompt = get_system_prompt()
    await get_inference_server_reply(system_prompt=system_prompt, msg="How bb, how are you?")
