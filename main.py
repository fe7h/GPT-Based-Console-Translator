#!/usr/bin/env python3
import utils
import core


def main():
    loop = True
    coppy = False

    args = utils.call_parser()

    if args.language1:
        pass
    if args.language2:
        pass

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
    print('Session started')

    for i in range(10):
        res =  translator.translate(args.data)
        print(utils.clean(res))

if __name__ == '__main__':
    main()
