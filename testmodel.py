from pydantic import BaseModel
from typing_extensions import Literal

class SamplingParameters(BaseModel):
    temperature: float
    top_p: float
    max_tokens = int


class LLMSettings(BaseModel):
    model_name: str
    tensor_parallel_size: int
    dtype: str
    trust_remote_code: bool
    enforce_eager: bool
    quantization: Literal["awq", "gptq"]
    # tokenizer: str


class PromptTemplate(BaseModel):
    name = Literal["vicuna", "alpaca"]
    vicuna: str = '''{system_prompt}
    USER: {user_prompt}
    ASSISTANT:
    '''


class SystemPrompt():
    general_description: str # this is an unnamed section in the system prompt
    bot_age: str
    bot_birth_date: str
    bot_desc: str
    bot_gender: str
    bot_likes: str
    bot_name: str
    bot_real_age: str
    bot_traits: str
    info_about_person_description: str # this is an unnamed section in the system prompt (Information about the person you are responding to:)
    user_age: str
    user_gender: str
    user_name: str
    miscellaneous_information: str
    date_time: str
    bot_task: str # this is an unnamed section in the system prompt (Your task is to roleplay as a human with the information stated above and respond naturally to the conversation partner's messages)
    