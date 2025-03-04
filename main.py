#!/usr/bin/env python3
import pyperclip

import config
import utils
import core


def main():
    loop = True
    coppy = False

    lang1 = config.DEFAULT_LANG1
    lang2 = config.DEFAULT_LANG2

    args = utils.call_parser()

    if args.language1:
        lang1 = args.language1
    if args.language2:
        lang2 = args.language2

    system_prompt = core.SystemPrompt(lang1, lang2)

    if args.coppy:
        coppy = True

    # if args.quick:
    #     loop = False
    # else:
    #     while loop:
    #         pass
    print(args)
    print('Connection to the session')
    translator = core.Translator()
    print('Session started\n')

    res =  translator.translate(system_prompt, args.data)
    res = utils.clean(res)
    print(res + '\n')
    if coppy:
        pyperclip.copy(res)


if __name__ == '__main__':
    main()
