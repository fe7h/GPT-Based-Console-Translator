__all__ = ['SEPARATOR', 'COMMAND_SYMBOL', 'DEFAULT_LANG1', 'DEFAULT_LANG2', 'SYSTEM_PROMPTS']

# Separator symbol between context and data for translation
SEPARATOR = '%'
# The symbol from which technical commands start in multiple mode
COMMAND_SYMBOL = '>'

# Languages that will be used by default
DEFAULT_LANG1 = 'english'
DEFAULT_LANG2 = 'russian'

# List of mandatory prompts for the correct operation of the translator. Better not to edit!
system_prompts_major = [
    'You are a translator',
    'You receive a request in the format connects:[connects] data:[data]'
    'You determine the language of the text in the data block',
    'If the language is {lang1} you translate it to {lang2}',
    'If the language is {lang2} you translate it to {lang1}',
    'If the context block is not empty, you create a translation in the specified context'
]
# List of other prompts for the translator. Can be supplemented if necessary
system_prompts_minor = [
    'The answer should not contain any characters or text unrelated to the translation',

]

SYSTEM_PROMPTS = '.'.join(system_prompts_major + system_prompts_minor)
