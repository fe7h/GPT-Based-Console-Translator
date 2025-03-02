from dataclasses import dataclass


@dataclass
class UserPrompt:
    text: str
    context: str = ''
