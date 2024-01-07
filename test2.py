from vllm import LLM, SamplingParams
# from pydantic import BaseModel, Field
from typing import Literal


class SamplingParameters():
    temperature: float
    top_p: float
    max_tokens = int


class LLMSettings():
    model_name: str
    tensor_parallel_size: int
    dtype: str
    trust_remote_code: bool
    enforce_eager: bool
    quantization: Literal["awq", "gptq"]
    # tokenizer: str


class PromptTemplate():
    name = Literal["vicuna", "alpaca"]
    vicuna = '''{system_prompt}
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


def format_system_prompt() -> str:
    pass

def format_prompts(prompt_template, system_prompt, prompts) -> JSON:
    formatted_prompts = [prompt_template.format(system_prompt=system_prompt, user_prompt=prompt) for prompt in prompts]
    return formatted_prompts

def generate(prompts: list, 
             system_prompt: SystemPrompt, 
             prompt_template: PromptTemplate.name, 
             sampling_parameters: SamplingParameters, 
             llm_settings: LLMSettings
             ) -> str:
    '''
        Generates response(s) from the LLM.
        Returns a JSON response back to the backend repo.
            - prompts: list | Takes in a list of prompts.
    '''
    # 1. Format system prompt:
    formatted_system_prompt = format_system_prompt(system_prompt)

    # 2. Set prompt template:
    match prompt_template:
        case "vicuna":
            prompt_template=PromptTemplate.vicuna
        case _:
            return "Error: Not a valid prompt template."
    
    # 3. Format prompt(s):
    formatted_prompts = format_prompts(prompt_template, formatted_system_prompt, prompts)

    # 4. Set sampling params:
    sampling_params = SamplingParams(temperature=sampling_parameters.temperature, 
                                     top_p=sampling_parameters.top_p, 
                                     max_tokens=sampling_parameters.max_tokens)
    # 5. Set llm settings:
    #TODO: Make this use the async engine later
    llm = LLM(model=llm_settings.model_name, 
              quantization=llm_settings.quantization, 
              tensor_parallel_size=llm_settings.tensor_parallel_size, 
              dtype=llm_settings.dtype,
              enforce_eager=llm_settings.enforce_eager
              )
    
    # 6. Generate response(s):
    #TODO use async engine for this as well
    outputs = llm.generate(formatted_prompts, sampling_params)

    #TODO 7. Compute advanced metrics:
    '''
        tokens_per_second
        stop_reason
        time_taken_per_generation
    '''

    #TODO 8. Return results (JSON):

generate()