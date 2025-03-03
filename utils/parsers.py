import argparse
import core


SEP = '"'

def call_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('data', type=data_parser)

    parser.add_argument('-q', '--quick', action='store_true')
    parser.add_argument('-c', '--coppy', action='store_true')
    parser.add_argument('-l1', '--language1')
    parser.add_argument('-l2', '--language2')

    return parser.parse_args()

def data_parser(data: str) -> core.prompts.UserPrompt:
    sep_pos = data.find(SEP)
    if sep_pos == -1:
        text = data
        context = ''
    else:
        text = data[sep_pos:]
        text = text.strip(SEP)
        context = data[:sep_pos]

    return core.prompts.UserPrompt(text, context)
