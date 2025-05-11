import tiktoken
from tiktoken import encoding_for_model

def get_tokens_len(content: str) -> int:
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = len(tokenizer.encode(content))
    return tokens

def get_token_size_limit(model_name: str, text: str) -> int:
    encoder = encoding_for_model("gpt-4o")
    tokens = encoder.encode(text)
    return len(tokens)