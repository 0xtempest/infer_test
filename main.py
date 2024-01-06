from huggingface_hub import hf_hub_download, snapshot_download
from goliath import goliath_function
from nous import nous_function

user_input = input("Which model do you want to use? (goliath-120b-AWQ/Nous-Capybara-34B)")

match user_input:
    case "goliath":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function()
    case "nous":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function()
    case _:
        "invalid input"

