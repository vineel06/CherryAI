import os
from llama_cpp import Llama

_fast_llm = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAST_MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
)


def _load_fast_model():
    global _fast_llm
    if _fast_llm is None:
        _fast_llm = Llama(
            model_path=FAST_MODEL_PATH,
            n_ctx=512,
            n_threads=12,
            n_batch=256,
            temperature=0.7,
            top_p=0.9,
            verbose=False
        )
    return _fast_llm


def fast_answer(prompt: str) -> str:
    llm = _load_fast_model()
    result = llm(
        prompt,
        max_tokens=64,
        stop=["</s>"]
    )
    return result["choices"][0]["text"].strip()
