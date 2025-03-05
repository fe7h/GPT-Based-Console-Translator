from g4f.client import Client

from . import prompts


class Translator:
    """Facade for interaction with the Client class from the g4f module"""
    def __init__(self):
        self.client = Client()

    def translate(self, system_prompt: prompts.SystemPrompt, user_message: prompts.UserPrompt):
        """Sends a request to ChatGPT and returns a response.

        The request content is divided into three parts:
        a prompt for the system role,
        a prompt containing the translation context,
        and a prompt containing the text for translation.

        Args:
            system_prompt (prompts.SystemPrompt)
            user_message (prompts.UserPrompt)

        Returns:
            str: Raw text response from chatGPT
        """
        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': system_prompt.content},
                {'role': 'user', 'content': f'контекст: {user_message.context}'},
                {'role': 'user', 'content': f'данные: {user_message.text}'}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content
