# GPT Based Console Translator

Console translator utility using chat GPT, also supports context for translation.

## About

Allows for quick and convenient translation of text while working in the console, utilizing the advantages of a language model to understand the context of what is written.

## Installation

## Usage
```commandline
usage: main.py [-h] [-m] [-c] [-s] [-l1 LANGUAGE1] [-l2 LANGUAGE2] [data]

positional arguments:
  data                  a string with text for translation.
                        Context can be specified for the translation,
                        for this you must first write the context,
                        and then highlight the translation with *.
                        Data is not necessary if the flag --multiple (-m) is set

options:
  -h, --help            show this help message and exit
  -m, --multiple        starts interactive mode. Special commands in interactive
                        mode must begin with COMMAND_SYMBOL
                        specified in the config (by default is '>').
                        Available commands: 
                        	exit - finish interactive mode
                        	copy - switch copy mode
                        	lang1, lang2 [new lang] - change lang of translation
  -c, --copy            copies translation to clipboard
  -s, --silence         disables the output message about the start of the session
  -l1 LANGUAGE1, --language1 LANGUAGE1
                        changes the translation language;
                        by default, the language from the config is used;
                        now is english
  -l2 LANGUAGE2, --language2 LANGUAGE2
                        changes the translation language;
                        by default, the language from the config is used;
                        now is russian
```