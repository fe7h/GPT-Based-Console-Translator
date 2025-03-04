from dataclasses import dataclass, field

import config


@dataclass
class UserPrompt:
    text: str
    context: str = ''


@dataclass
class SystemPrompt:
    _lang1: str
    _lang2: str
    content: str = field(init=False)

    def __post_init__(self):
        self._content_format()

    def _content_format(self):
        self.content = config.SYSTEM_PROMPTS.format(lang1=self._lang1, lang2=self._lang2)

    @staticmethod
    def __get_lang(attr:str):
        def internal(self):
            return getattr(self, attr)
        return internal

    @staticmethod
    def __set_lang(attr:str):
        def internal(self, value:str):
            setattr(self, attr, value)
            self._content_format()
        return internal

    lang1 = property(__get_lang('_lang1'), __set_lang('_lang1'))
    lang2 = property(__get_lang('_lang2'), __set_lang('_lang2'))
