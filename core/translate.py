from g4f.client import Client

from . import prompts


class Translator:
    def __init__(self):
        self.client = Client()

    def translate(self, system_prompt: prompts.SystemPrompt, user_message: prompts.UserPrompt):
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
