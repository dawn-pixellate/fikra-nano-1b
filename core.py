import os
import sys
from huggingface_hub import hf_hub_download

# Try to import llama_cpp, handle missing dependency gracefully
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None

class Fikra:
    def __init__(self, model_path=None, verbose=False):
        if Llama is None:
            raise ImportError("❌ 'llama-cpp-python' is not installed. Run: pip install llama-cpp-python")

        print("🧠 Initializing Fikra 1B Engine...")
        
        # 1. Automatic Download
        if model_path is None:
            print("⬇️  Checking for model updates...")
            try:
                model_path = hf_hub_download(
                    repo_id="lacesseapp/Fikra-1B-Nano-v0.2-GGUF",
                    filename="fikra-1b-nano-v0.2-q4_k_m.gguf"
                )
            except Exception as e:
                raise ConnectionError(f"Failed to download model: {e}")
                
        print(f"📂 Loading Brain: {model_path}")

        # 2. Load Engine (CPU Optimized)
        try:
            self.brain = Llama(
                model_path=model_path,
                n_ctx=2048,
                n_threads=max(1, os.cpu_count() - 1),
                verbose=verbose,
                chat_format="chatml"
            )
        except Exception as e:
            raise RuntimeError(f"❌ Engine Failure: {e}")

    def reason(self, prompt, max_tokens=512):
        '''Strict logic mode'''
        formatted = f"User: {prompt}\\nAnswer:"
        output = self.brain(
            formatted,
            max_tokens=max_tokens,
            stop=["<|endoftext|>", "User:"],
            temperature=0.1, # Low temp for math/logic
            echo=False
        )
        return output['choices'][0]['text'].strip()
