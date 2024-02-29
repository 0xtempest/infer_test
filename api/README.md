pip install -e .

python3 -m venv py_env

source py_env/bin/activate

pip3 install -r requirements.txt
pip3 install vllm

python3 api/main.py

python -m vllm.entrypoints.api_server \
    --model Nous-Capybara-34B \
    --tensor-parallel-size 8 \
    --dtype "float16" \
    --tokenizer "tokenizer.model" \
    --max-model-len 70000 \
    --gpu-memory-utilization 0.99 \ 
    --trust-remote-code "yes" \
    --port 8005 \
    --enforce-eager

python -m vllm.entrypoints.api_server \
    --model Nous-Capybara-34B \
    --tensor-parallel-size 8 \
    --dtype "float16" \
    --max-model-len 70000 \
    --gpu-memory-utilization 0.99 \ 
    --port 8005 \
    --enforce-eager

python3 -m vllm.entrypoints.openai.api_server --model TheBloke/goliath-120b-AWQ --host 0.0.0.0 --port 8005 --tensor-parallel-size 8 --quantization awq --dtype auto --enforce-eager

python3 -m vllm.entrypoints.openai.api_server --model TheBloke/goliath-120b-AWQ --host 0.0.0.0 --port 8005 --tensor-parallel-size 8 --dtype float16 --max-model-len 4096 --gpu-memory-utilization 0.99 --trust-remote-code --enforce-eager --quantization awq

python3 -m vllm.entrypoints.openai.api_server --model NousResearch/Nous-Capybara-34B --host 0.0.0.0 --port 8005 --tensor-parallel-size 8 --dtype float16 --max-model-len 70000 --gpu-memory-utilization 0.99 --trust-remote-code --enforce-eager --tokenizer