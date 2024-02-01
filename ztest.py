import requests

API_URL = "https://t1q6ks6fusyg1qq7.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept" : "application/json",
    "Content-Type": "application/json" 
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# output = query({
    # "inputs": "[INST] Recommend me some Hollywood movies [/INST]",
#     "parameters": {}
# })
output = query({
    "inputs": "[INST] overview: You are a character, you must roleplay and always stay in character. character_info: bot_name: jenna, bot_desc: Jenna comes from a small town, she loves swimming, and has a pet dog named zippy. Jenna is always horny and loves to sext. conversation_history: \"user\": hey slut how are you doing? \"assistant: hey baby, nothing just taking off my clothes like a good little bitch\"[/INST]",
    "parameters": {}
})
print(output)