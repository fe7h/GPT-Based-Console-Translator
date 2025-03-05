import argparse

import config
import core


def call_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('data', nargs='?', type=data_parser)

    parser.add_argument('-m', '--multiple', action='store_true')
    parser.add_argument('-c', '--coppy', action='store_true')
    parser.add_argument('-l1', '--language1')
    parser.add_argument('-l2', '--language2')

    return parser.parse_args()

def data_parser(data: str) -> core.prompts.UserPrompt:
    sep_pos = data.find(config.SEPARATOR)
    if sep_pos == -1:
        text = data
        context = ''
    else:
        text = data[sep_pos:]
        text = text.strip(config.SEPARATOR)
        context = data[:sep_pos]
    print(core.prompts.UserPrompt(text, context))
    return core.prompts.UserPrompt(text, context)

def session_call_parser():
    pass
