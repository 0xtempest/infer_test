from vllm import LLM, SamplingParams
# from pydantic import BaseModel, Field
from typing import Literal

from testmodel import PromptTemplate, SamplingParameters, SystemPrompt, LLMSettings


def generate(prompts: list, 
             system_prompt: SystemPrompt, 
             prompt_template: PromptTemplate, 
             sampling_parameters: SamplingParameters, 
             llm_settings: LLMSettings
             ) -> JSON:
    ''' everything sud be a one line function call
        Generates response(s) from the LLM.
        Returns a JSON response back to the backend repo.
            - prompts: list | Takes in a list of prompts.
    '''
    # 1. Format system prompt:
    formatted_system_prompt = set_format_system_prompt(system_prompt)

    # 2. Set prompt template:
    formatted_prompt_template = set_prompt_template(prompt_template)

    # 3. Format prompt(s):
    formatted_prompts = set_format_prompts(formatted_prompt_template, formatted_system_prompt, prompts)

    # 4. Set sampling params:
    sampling_params = set_sampling_params(sampling_parameters)

    # 5. Set llm engine with llm settings:
    llm = set_llm_settings(llm_settings)

    # 6. Generate response(s):
    outputs = get_outputs(llm, formatted_prompts, sampling_params)

    #TODO 7. Compute advanced metrics:
    '''
        tokens_per_second
        stop_reason
        time_taken_per_generation
    '''

    #TODO 8. Return results (JSON): use fastapi jsonify object

generate()