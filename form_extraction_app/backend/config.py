import os

# Hugging Face Inference API Config

HF_API_KEY = os.getenv("HF_API_KEY")

if HF_API_KEY is None:
    raise EnvironmentError(
        "HF_API_KEY is not set. Please set it as an environment variable."
    )

# default model
HF_MODEL = "tiiuae/falcon-7b-instruct"

# Inference settings
HF_MAX_NEW_TOKENS = 512
HF_TEMPERATURE = 0.0  # deterministic output for JSON
