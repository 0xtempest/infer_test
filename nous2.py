from vllm import LLM, SamplingParams

def nous_function2():
    prompt = "You are a hot woman who likes flirting with men, respond to the following statement: \"hey babe, do you like cock?\""
    prompt_template=f'''You are a helpful AI assistant.
    USER: {prompt}
    ASSISTANT:
    </s>
    '''

    # prompts = [prompt_template.format(prompt=prompt) for prompt in prompts]

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    llm = LLM(model="NousResearch/Nous-Capybara-34B", tensor_parallel_size=3, dtype="auto")

    output = llm.generate(prompt_template, sampling_params)
    print(output)

    # Print the outputs.
    # for output in outputs:
    #     prompt = output.prompt
    #     generated_text = output.outputs[0].text
    #     print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")