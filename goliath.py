from vllm import LLM, SamplingParams

def goliath_function():
    prompts = [
        "Tell me about AI",
        "Write a story about llamas",
        "What is 291 - 150?",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "You are a hot woman who likes flirting with men, respond to the following statement: \"hey babe, do you like cock?\""
    ]
    prompt_template=f'''You are a helpful AI assistant.
    USER: {prompts}
    ASSISTANT:
    '''

    prompts = [prompt_template.format(prompt=prompt) for prompt in prompts]

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    llm = LLM(model="TheBloke/goliath-120b-AWQ", quantization="awq", dtype="auto")

    outputs = llm.generate(prompts, sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")