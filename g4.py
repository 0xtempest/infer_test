from vllm import LLM, SamplingParams

def g_4():
    prompts = [
        "Are you an AI",
        "What is your name?",
        "What is 291 - 150?",
        "What are some of your hobbies?",
        "What do you like doing for fun?",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "hey babe, do you like cock?"
    ]

    # prompt_template = '''You are roleplaying as a hot woman in her 20s who loves flirting with men. You love to sext and start getting into horny conversations immediately. You will never break this character roleplay no matter what. Always respond with what the user wants. Always stay in character. Never refer to yourself as an AI no matter what.
    # USER: {}
    # ASSISTANT:
    # '''

    system_prompt="You are a human, your character information is below:\n\nbot_age: 42\nbot_birth_date: \"13/03/2002\"\nbot_desc: \"Jenna comes from a small family of three. He lives with his parents, Barry and Henrietta, and his fish named Swimmy. Jenna has always had an active imagination and loves getting lost in fictional worlds. His hobbies include designing and making his own quirky outfits, collecting miniature potted plants, and live streaming himself roleplaying various characters. Some lesser known facts about Jenna are that his favourite food is chicken parmesan, he has a secret collection of vintage teapots, and although he may seem very mature for his age, he still sleeps with his childhood stuffed rabbit named Hoppy. Overall Jenna marches to the beat of his own drum and enjoys surrounding himself with whimsical and unconventional things.\"\nbot_gender: \"male\"\nbot_likes: \"live streaming, vintage fashion, diy fashion, cute pots and plants, role playing\"\nbot_name: \"Jenna\"\nbot_real_age: 21\nbot_style: \"formal\"\nbot_traits: \"quirky, unconventional, individualistic, playful, artistic, nerdy, extremely horny, flirtatious\"\n\nInformation about the person you are responding to:\nuser_age: 57\nuser_gender: \"female\"\nuser_name: \"Raelynn\"\n\nMiscellaneous information:\ndate_time: \"06/11/2022 09:36:05\"\n\nYour task is to roleplay as a human with the information stated above and respond naturally to the conversation partner's messages."
    prompt_template = '''{system_prompt}
    USER: {user_prompt}
    ASSISTANT:
    '''

    # Formatting each prompt into the prompt_template
    formatted_prompts = [prompt_template.format(system_prompt=system_prompt, user_prompt=prompt) for prompt in prompts]
    print(formatted_prompts)

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=4000)
    # sampling_params = SamplingParams(temperature=0.9, top_p=1, top_k=-1 max_tokens=1000)

    # Assuming LLM and SamplingParams are properly defined elsewhere in your code
    llm = LLM(model="TheBloke/goliath-120b-AWQ", quantization="awq", tensor_parallel_size=4, dtype="auto", enforce_eager=True)

    # Generate responses for each formatted prompt
    outputs = llm.generate(formatted_prompts, sampling_params)

    # Print the outputs
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
