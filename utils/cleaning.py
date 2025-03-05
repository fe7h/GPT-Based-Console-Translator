def clean(text: str) -> str:
    """Removes artifacts from the response text.

    The function should be supplemented in case of new artifacts.

    Args:
        text (str): Raw text response from chatGPT.

    Returns:
        str: Cleaned text.
    """
    if (bad_text := '[[Login to OpenAI ChatGPT]]()') in text:
        text = text.replace(bad_text, '')

    return text.strip()
