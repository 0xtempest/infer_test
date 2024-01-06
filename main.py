from huggingface_hub import hf_hub_download, snapshot_download
from goliath import goliath_function
from goliath2 import goliath_function2

from nous import nous_function
from nous2 import nous_function2

user_input = input("Which model do you want to use? (goliath/nous)")

match user_input:
    case "goliath":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function()
    case "goliath2":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function2()
    case "nous":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function()
    case "nous2":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function2()
    case _:
        "invalid input"

