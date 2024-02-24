from api.helpers import count_characters_and_tokens
from api.settings import TextInferenceServerConfig, Models
import httpx

async def get_inference_server_reply(system_prompt, msg):
    models = Models()
    url = TextInferenceServerConfig.URL
    char_count, token_count = count_characters_and_tokens(system_prompt)
    print(f"Character Count: {char_count}")
    print(f"Token Count: {token_count}")
    prompt_template = models.Goliath120b.prompt_template

    formatted_prompts = prompt_template.format(
        system_prompt=system_prompt, user_prompt=msg
    )

    request_body = {
        "model": models.Goliath120b.name,
        "prompt": formatted_prompts,
        "max_tokens": models.Goliath120b.context_length
        - token_count
        - 151,  # Look at the max tokens logic more closely, hardcoding for now
        "temperature": models.Goliath120b.temperature,
        "top_p": models.Goliath120b.top_p,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=request_body, timeout=60.0)
        print(resp.text)
        return resp.text