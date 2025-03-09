import argparse

import config
import core


def call_parser() -> argparse.Namespace:
    """Creates an argparse.ArgumentParser object and sets its arguments.

    Returns:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('data',
                        nargs='?',
                        type=data_parser,
                        help='a string with text for translation.\n'
                             'Context can be specified for the translation,\n'
                             'for this you must first write the context,\n'
                             f'and then highlight the translation with {config.SEPARATOR}.\n'
                             'Data is not necessary if the flag --multiple (-m) is set')

    parser.add_argument('-m', '--multiple',
                        action='store_true',
                        help='starts interactive mode. '
                             'Special commands in interactive\nmode must begin '
                             'with COMMAND_SYMBOL\nspecified in the config (by default is \'>\').\n'
                             'Available commands: \n\texit - finish interactive mode'
                             '\n\tcopy - switch copy mode'
                             '\n\tlang1, lang2 [new lang] - change lang of translation')
    parser.add_argument('-c', '--copy',
                        action='store_true',
                        help='copies translation to clipboard')
    parser.add_argument('-s', '--silence',
                        action='store_true',
                        help='disables the output message about the start of the session')
    language_help_msg = ('changes the translation language;\n'
                         'by default, the language from the config is used;\n'
                         'now is {DEFAULT_LANG}')
    parser.add_argument('-l1', '--language1',
                        help=language_help_msg.format(DEFAULT_LANG=config.DEFAULT_LANG1))
    parser.add_argument('-l2', '--language2',
                        help=language_help_msg.format(DEFAULT_LANG=config.DEFAULT_LANG2))

    return parser.parse_args()


def data_parser(data: str) -> core.prompts.UserPrompt:
    """Processes the data for translation received from the user.

    Splits the text by the first occurrence of SEPARATOR specified in the config.

    Args:
        data (str): Raw text, possibly containing the symbol SEPARATOR.

    Returns:
        core.prompts.UserPrompt: Prepared data for user prompt.
    """
    sep_pos = data.find(config.SEPARATOR)
    if sep_pos == -1:
        text = data
        context = ''
    else:
        text = data[sep_pos:]
        text = text.strip(config.SEPARATOR)
        context = data[:sep_pos]

    return core.prompts.UserPrompt(text, context)
