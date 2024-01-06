
import os
import shutil
from huggingface_hub import hf_hub_download, snapshot_download
from ctransformers import AutoModelForCausalLM

# def download_model(repo_id, filename, local_dir):
#     """
#     Download a file from a repository on the Hugging Face model hub.

#     :param repo_id: Repository ID on Hugging Face, e.g., 'TheBloke/goliath-120b-GGUF'
#     :param filename: Name of the file to download, e.g., 'goliath-120b.Q5_K_M.gguf'
#     :param local_dir: Local directory to save the downloaded file
#     """
#     # Ensure the local directory exists, create if it doesn't
#     os.makedirs(local_dir, exist_ok=True)

#     # Construct the path for the local file
#     local_file_path = os.path.join(local_dir, filename)

#     # Download the file
#     hf_hub_download(repo_id=repo_id, filename=filename, cache_dir=local_dir)

#     # If symlinks are not to be used, ensure the file is physically present in the specified directory
#     if not os.path.islink(local_file_path):
#         shutil.copyfile(os.path.join(local_dir, filename), local_file_path)

# Example usage
# repo_id = "TheBloke/goliath-120b-GGUF"
# filename = "goliath-120b.Q4_K_M.gguf"
# local_dir = "~/repo/infer_test/models/"

# download_model(repo_id, filename, local_dir)


def goliath_functionc():
    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    llm = AutoModelForCausalLM.from_pretrained("TheBloke/goliath-120b-GGUF", model_file="goliath-120b.Q5_K_M.gguf", model_type="llama", gpu_layers=70, repetition_penalty=1.1, temperature=0.7)

    print(llm("AI is going to"))

