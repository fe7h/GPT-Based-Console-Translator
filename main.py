#!/usr/bin/env python3
import pyperclip
import readline

import config
import utils
import core


def main():

    args = utils.call_parser()

    lang1:str = args.language1 if args.language1 else config.DEFAULT_LANG1
    lang2:str  = args.language2 if args.language2 else config.DEFAULT_LANG2

    system_prompt = core.SystemPrompt(lang1, lang2)

    coppy:bool = args.coppy

    print('Connection to the session...')
    translator = core.Translator()
    print('Session started')


    def common_logic():
        # General code for a single request and for multiple requests in a loop
        res = translator.translate(system_prompt, req)
        res = utils.clean(res)
        print('\n' + res + '\n')
        if coppy: pyperclip.copy(res)

    # Handling single mode
    if not args.multiple:
        req = args.data
        common_logic()
    # Handling multiple mode
    else:
        # Handling tech commands
        while True:
            req = input('>')
            if req.startswith(config.COMMAND_SYMBOL):
                req = req.strip(config.COMMAND_SYMBOL).split()
                if len(req) == 0:
                    print('Command not found')
                elif req[0] == 'exit':
                    break
                elif req[0] == 'coppy':
                    coppy = False if coppy else True
                    print('Now coppy is', coppy)
                elif 'lang' in req[0]:
                    try:
                        setattr(system_prompt, req[0], req[1])
                        print(f'Now lang1 is {system_prompt.lang1}, lang2 is {system_prompt.lang2}')
                    except (AttributeError, IndexError):
                        print('Incorrect number or language is not specified')
            # Processing a translation request
            else:
                req = utils.data_parser(req)
                common_logic()


if __name__ == '__main__':
    main()
