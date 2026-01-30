from llama_cpp import Llama
from pathlib import Path

_llm = None


def _find_project_root(start: Path) -> Path:
    for parent in [start] + list(start.parents):
        if (parent / "models").exists():
            return parent
    raise FileNotFoundError("Could not locate project root with models/")


def _load_model():
    global _llm
    if _llm is not None:
        return _llm

    root = _find_project_root(Path(__file__).resolve())
    models = root / "models"

    mistral = models / "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    tiny = models / "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

    if mistral.exists():
        model_path = mistral
        ctx = 4096
        gpu_layers = 35
    elif tiny.exists():
        model_path = tiny
        ctx = 2048
        gpu_layers = 20
    else:
        raise FileNotFoundError("No GGUF model found in models/")

    _llm = Llama(
        model_path=str(model_path),
        n_ctx=ctx,
        n_gpu_layers=gpu_layers,
        n_threads=8,
        verbose=False
    )
    return _llm


def generate_text(prompt: str) -> str:
    llm = _load_model()

    # ❌ no <s> here anymore
    result = llm(
        f"[INST] {prompt} [/INST]",
        max_tokens=512,
        temperature=0.7,
        stop=["</s>"]
    )

    return result["choices"][0]["text"].strip()
