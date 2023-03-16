"""
emulation TD4
"""

import td4.parse as td4


def emulator(enter):
    for i in enter:
        print(td4.parser(i))
