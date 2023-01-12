import argparse
import json
from colorama import init
from termcolor import colored

init()

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
parser.add_argument('-c', '--center_letter', required=True)
parser.add_argument('-o', '--other_letters', required=True)

def main():
    args = parser.parse_args()

    _validate_args(args)

    with open('./words_dictionary.json') as user_file:
        words_dict = json.loads(user_file.read())

    words_list = words_dict.keys()

    required_letter = args.center_letter
    possible_letters = list(args.other_letters) + [args.center_letter]

    nonpangrams = []
    pangrams = []

    for word in words_list:
        if len(word) <= 3:
            continue

        characters = list(word)

        if required_letter not in characters:
            continue

        if any([c not in possible_letters for c in characters]):
            continue

        if all([pl in characters for pl in possible_letters]):
            pangrams.append(word)

        nonpangrams.append(word)

    print('Non-pangrams')
    for idx, r in enumerate(nonpangrams):
        print(f'{idx} {r}')

    print(colored('\npangrams', 'green'))
    for idx, r in enumerate(pangrams):
        print(colored(f'{idx} {r}', 'green'))


def _validate_args(args):
    if len(args.center_letter) != 1:
        raise f'There should be one center letter, you have {len(args.center_letter)}'

    if len(args.other_letters) != 6:
        raise f'there should be 6 other letters, you have {len(args.other_letters)}'



