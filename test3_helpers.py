from vllm import LLM, SamplingParams
# from pydantic import BaseModel, Field
from typing import Literal
from testmodel import PromptTemplate, SamplingParameters, SystemPrompt, LLMSettings


def set_format_system_prompt(system_prompt):
    pass


def set_prompt_template(prompt_template: PromptTemplate):
    match prompt_template.name:
        case "vicuna":
            formatted_prompt_template=prompt_template.vicuna
        case "alpaca":
            return "Error: Alpaca not supported yet."
        case _:
            return "Error: Not a valid prompt template."
    return formatted_prompt_template


def set_format_prompts(formatted_prompt_template, formatted_system_prompt, prompts):
    formatted_prompts = [formatted_prompt_template.format(system_prompt=formatted_system_prompt, user_prompt=prompt) for prompt in prompts]
    return formatted_prompts


def set_sampling_params(sampling_parameters):
    sampling_params = SamplingParams(temperature=sampling_parameters.temperature, 
                                    top_p=sampling_parameters.top_p, 
                                    max_tokens=sampling_parameters.max_tokens)
    return sampling_params


#TODO: Make this use the async engine later
def set_llm_settings(llm_settings):
    llm = LLM(model=llm_settings.model_name, 
              quantization=llm_settings.quantization, 
              tensor_parallel_size=llm_settings.tensor_parallel_size, 
              dtype=llm_settings.dtype,
              enforce_eager=llm_settings.enforce_eager
              )
    return llm


#TODO use async engine for this as well
def get_outputs(llm, formatted_prompts, sampling_params):
    outputs = llm.generate(formatted_prompts, sampling_params)
    return outputs
