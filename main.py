import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

from huggingface_hub import hf_hub_download, snapshot_download
from goliath import goliath_function
from goliath2 import goliath_function2
from goliath3 import goliath_function3


from nous import nous_function
from nous2 import nous_function2
from nous3 import nous_function3


user_input = input("Which model do you want to use? (goliath/nous)")

match user_input:
    case "goliath":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function()
    case "goliath2":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function2()
    case "goliath3":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        goliath_function3()
    case "nous":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function()
    case "nous2":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function2()
    case "nous3":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function3()
    case _:
        "invalid input"

