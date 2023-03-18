"""
Parse Input
"""

import re
import td4.opcode


def to_binary(i):
    instruction = re.split(r"[, ]", i)

    if len(instruction) == 3 and instruction[2].isalpha():
        # MOV A, B | MOV B, A
        return (
            td4.opcode.to_opcode("".join(list(map(lambda x: x.upper(), instruction))))
            + "0000"
        )
    elif len(instruction) == 3 and instruction[1].isalpha():
        # MOV A, Im | MOV B, Im | ADD A, Im | ADD B, Im
        return (
            td4.opcode.to_opcode(
                "".join(list(map(lambda x: x.upper(), instruction[:2])))
            )
            + instruction[2]
        )
    elif len(instruction) == 2 and instruction[1].isalpha():
        # IN A | IN B | OUT B
        return (
            td4.opcode.to_opcode("".join(list(map(lambda x: x.upper(), instruction))))
            + "0000"
        )
    elif len(instruction) == 2 and instruction[0].isalpha():
        # OUT Im | JMP Im | JNC Im
        return td4.opcode.to_opcode(instruction[0].upper()) + instruction[1]
    else:
        # Not Assembly
        return "".join(instruction)


def to_binary_td4(file):
    INSTRUCTION_LENGTH = 8

    instruction = [
        ("".join(file[index : index + INSTRUCTION_LENGTH]))[::-1]
        for index in range(0, 128, INSTRUCTION_LENGTH)
    ]
    if file[128] == "#TRUE#":
        clock = "1"
    elif file[129] == "#TRUE#":
        clock = "10"
    else:
        clock = "manual"
    beep = True if file[131] == "1" else False

    return instruction, clock, beep


def to_assembly(instruction):
    return td4.opcode.to_assembly(instruction[:4], instruction[4:])
