def clean(text: str):
    if (bad_text := '[[Login to OpenAI ChatGPT]]()') in text:
        text = text.replace(bad_text, '')

    return text.strip()
