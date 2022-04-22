from collections import Counter
from functools import lru_cache
import argparse

parser = argparse.ArgumentParser(prog="Unique Characters Generator",
                                 description="This tool will display quantity of unique characters "
                                             "in the letters string or text file")

parser.add_argument("-s", "--string", type=str, help="Enter a string of latin letters, e.g. 'ddfopphhh'",
                    metavar="str")
parser.add_argument("-f", "--file", type=str, help="Enter path to the text file",
                    metavar="PATH")
args = parser.parse_args()


@lru_cache
def unique_characters(s):
    if not isinstance(s, str):
        raise TypeError("Text should be a str")
    return sum(i for i in Counter(s).values() if i == 1)


def parse_input(arguments):
    if arguments.file:
        with open(arguments.file) as f:
            s_file = f.read()
            return unique_characters(s_file)
    elif arguments.string:
        return unique_characters(arguments.string)
    else:
        raise AttributeError("Please enter an argument")

