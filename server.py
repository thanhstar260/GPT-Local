import subprocess

command = 'python -m llama_cpp.server --model "./models/mistral-7b-openorca.Q4_0.gguf" --chat_format chatml --n_gpu_layers 0'
subprocess.call(command, shell=True)