from helpers import count_characters_and_tokens
from settings import TextInferenceServerConfig, Models
import httpx

async def get_inference_server_reply(model, system_prompt, msg):
    models = Models()
    url = TextInferenceServerConfig.URL
    char_count, token_count = count_characters_and_tokens(system_prompt)
    print(f"Character Count: {char_count}")
    print(f"Token Count: {token_count}")
    match model:
        case "Goliath120b":
            prompt_template = models.Goliath120b.prompt_template
        case "NousCapy34b":
            prompt_template = models.NousCapy34b.prompt_template
        case "Miqu120b":
            prompt_template = models.Miqu120b.prompt_template
        case _:
            return "Error: Not a valid model."

    formatted_prompts = prompt_template.format(
        system_prompt=system_prompt, user_prompt=msg
    )

    match model:
        case "Goliath120b":
            request_body = {
                "model": models.Goliath120b.name,
                "prompt": formatted_prompts,
                # "max_tokens": models.Goliath120b.context_length
                # - token_count
                # - 151,  
                "max_tokens": models.max_tokens,
                "temperature": models.Goliath120b.temperature,
                "top_p": models.Goliath120b.top_p,
            }
        case "NousCapy34b":
            request_body = {
                "model": models.NousCapy34b.name,
                "prompt": formatted_prompts,
                "max_tokens": models.max_tokens,
                "temperature": models.NousCapy34b.temperature,
                "top_p": models.NousCapy34b.top_p,
            }

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=request_body, timeout=60.0)
        print(resp.text)
        return resp.text