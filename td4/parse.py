"""
Parse Input
"""

import re
import td4.opcode


def parser(i):
    instruction = re.split(r"[, ]", i)

    if len(instruction) == 3 and instruction[2].isalpha():
        # MOV A, B | MOV B, A
        return (
            td4.opcode.opcode("".join(list(map(lambda x: x.upper(), instruction))))
            + "0000"
        )
    elif len(instruction) == 3 and instruction[1].isalpha():
        # MOV A, Im | MOV B, Im | ADD A, Im | ADD B, Im
        return (
            td4.opcode.opcode("".join(list(map(lambda x: x.upper(), instruction[:2]))))
            + instruction[2]
        )
    elif len(instruction) == 2 and instruction[1].isalpha():
        # IN A | IN B | OUT B
        return (
            td4.opcode.opcode("".join(list(map(lambda x: x.upper(), instruction))))
            + "0000"
        )
    elif len(instruction) == 2 and instruction[0].isalpha():
        # OUT Im | JMP Im | JNC Im
        return td4.opcode.opcode(instruction[0].upper()) + instruction[1]
    else:
        # Not Assembly
        return "".join(instruction)


def td4_parser(file):
    instruction = [("".join(file[index : index + 8]))[::-1] for index in range(0, 128, 8)]
    clock = str([i+1 for i in range(len(file)) if file[i] == "#TRUE#"][0] - 128)
    beep = True if file[131] == "1" else False

    return instruction, clock, beep
