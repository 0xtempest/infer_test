import os
import logging
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2"
# os.environ["RAY_USE_MULTIPROCESSING_CPU_COUNT"] = "1"
os.environ['TORCH_CPP_LOG_LEVEL'] = 'INFO'

# Configure Python logging
logging.basicConfig(level=logging.DEBUG)

from huggingface_hub import hf_hub_download, snapshot_download
from g1 import g_1
from g2 import g_2
from g3 import g_3
from g4 import g_4
# from g5 import g_5
# logging.debug("Starting JIT compilation")
# from g7 import g_7
# logging.debug("JIT compilation finished")

from d1 import d_1
from n4 import n_4
from s1 import s_1



# from goliathc import goliath_functionc, download_model

from nous import nous_function
from nous2 import nous_function2
from nous3 import nous_function3


user_input = input("Which model do you want to use? (goliath/nous)")

match user_input:
    case "g1":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        g_1()

    case "g2":
        # hf_hub_download("TheBloke/goliath-120b-AWQ")
        g_2()

    case "g3":
        snapshot_download("TheBloke/goliath-120b-AWQ")
        g_3()
        
    case "g4":
        snapshot_download("TheBloke/goliath-120b-AWQ")
        g_4()
        
    case "d1":
        snapshot_download("TheBloke/MegaDolphin-120b-AWQ")
        d_1()

    case "n4":
        snapshot_download("TheBloke/Nous-Capybara-34B-AWQ")
        n_4()

    case "s1":
        snapshot_download("Weyaxi/SauerkrautLM-UNA-SOLAR-Instruct")
        s_1()

    # case "g5":
    #     repo_id = "Panchovix/goliath-120b-exl2-rpcal/tree/4.85bpw"
    #     local_dir = "./models"
    #     snapshot_download(rep_id=repo_id, local_dir=local_dir, local_dir_use_symlinks=False)

    # case "goliathc":
    #     repo_id = "TheBloke/goliath-120b-GGUF"
    #     filename = "goliath-120b.Q5_K_M.gguf"
    #     # local_dir = "~/repo/infer_test/models/"
    #     # download_model(repo_id, filename, local_dir)
    #     hf_hub_download(repo_id=repo_id, filename=filename)
    #     goliath_functionc()

    # case "g7":
    #     # repo_id = "Panchovix/goliath-120b-exl2-rpcal/tree/4.85bpw"
    #     repo_id = "Panchovix/goliath-120b-exl2-rpcal"
    #     revision = "4.85bpw"
    #     local_dir = "./models"
    #     snapshot_download(repo_id=repo_id, revision=revision, local_dir=local_dir, local_dir_use_symlinks=False)
    #     g_7()
    
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

