from pydantic import BaseModel
from typing_extensions import Literal
from typing import Optional

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


class SystemPromptAdminValues(BaseModel):
    overview: Optional[str] = None
    bot_task: Optional[str] = None
    function_calling_description: Optional[str] = None
    function_format: Optional[str] = None
    available_functions: Optional[str] = None
    end_emotional_prompt: Optional[str] = None




class SystemPromptValues(BaseModel):
    '''
    name: this is the name of the system_prompt itself, usually called "system_prompt:"
    general_description: this is an unnamed section in the system prompt

    user_info_section_description: this is an unnamed section in the system prompt (Information about the person you are responding to:)
    bot_task: this is an unnamed section in the system prompt (Your task is to roleplay as a human with the information stated above and respond naturally to the conversation partner's messages)

    '''
    overview: Optional[str] = None

    bot_maturity_level_age: Optional[str] = None
    bot_real_age: Optional[str] = None
    bot_birth_date: Optional[str] = None
    bot_name: Optional[str] = None
    bot_gender: Optional[str] = None
    bot_desc: Optional[str] = None
    bot_world_desc: Optional[str] = None
    bot_likes: Optional[str] = None
    bot_traits: Optional[str] = None
    bot_type: Optional[str] = str
    bot_tone: Optional[str] = str
    bot_roleplay_scenario: Optional[str] = None
    bot_roleplay_task: Optional[str] = None
    bot_task: Optional[str] = str
    current_date: Optional[str] = None

    user_age: Optional[str] = None
    user_gender: Optional[str] = None
    user_name: Optional[str] = None

    function_calling_description: Optional[str] = None
    function_format: Optional[str] = None
    available_functions: Optional[str] = None

    available_long_term_memories: Optional[str] = None

    available_conversation_history: Optional[str] = None

    end_emotional_prompt: Optional[str] = None



class SystemPromptKeys(BaseModel):
    name: Optional[str] = None
    general_description_section_description: Optional[str] = None
    bot_maturity_level_age: str
    bot_real_age: str
    bot_birth_date: str
    bot_name: str
    bot_gender: str
    bot_desc: str
    bot_world_desc: str
    bot_likes: str
    bot_traits: str
    bot_roleplay_task: str
    bot_task: str
    current_date: str

    user_info_section_description: str 
    user_age: str
    user_gender: str
    user_name: str

    # miscellaneous_information_section_description: str
    # current_date: str
    # bot_task: str

    function_calling_section_description: str
    function_calling_description: str
    function_format: str
    available_functions: str

    long_term_memories_section_description: str
    available_long_term_memories: str

    conversation_history_section_description: str
    available_conversation_history: str

    end_emotional_prompt: Optional[str] = None

