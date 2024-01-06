import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2"
os.environ["RAY_USE_MULTIPROCESSING_CPU_COUNT"] = "1"

from huggingface_hub import hf_hub_download, snapshot_download
from goliath import goliath_function
from goliath2 import goliath_function2
from goliath3 import goliath_function3
# from goliathc import goliath_functionc, download_model

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
        snapshot_download("TheBloke/goliath-120b-AWQ")
        goliath_function3()

    # case "goliathc":
    #     repo_id = "TheBloke/goliath-120b-GGUF"
    #     filename = "goliath-120b.Q5_K_M.gguf"
    #     # local_dir = "~/repo/infer_test/models/"
    #     # download_model(repo_id, filename, local_dir)
    #     hf_hub_download(repo_id=repo_id, filename=filename)
    #     goliath_functionc()

    case "nous":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function()

    case "nous2":
        # hf_hub_download("NousResearch/Nous-Capybara-34B")
        nous_function2()

    case "nous3":
        snapshot_download("NousResearch/Nous-Capybara-34B")
        nous_function3()

    case _:
        "invalid input"

