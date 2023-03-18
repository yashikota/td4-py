"""
instruction set
"""


def to_opcode(arg):
    op = {
        "MOVA": "0011",
        "MOVB": "0111",
        "MOVAB": "0001",
        "MOVBA": "0100",
        "ADDA": "0000",
        "ADDB": "0101",
        "INA": "0010",
        "INB": "0110",
        "OUT": "1011",
        "OUTB": "1001",
        "JMP": "1111",
        "JNC": "1110",
    }

    return op[arg]


def to_assembly(opcode, operand):
    op = {
        "0011": "MOV A",
        "0111": "MOV B",
        "0001": "MOV A, B",
        "0100": "MOV B, A",
        "0000": "ADD A",
        "0101": "ADD B",
        "0010": "IN A",
        "0110": "IN B",
        "1011": "OUT",
        "1001": "OUT B",
        "1111": "JMP",
        "1110": "JNC",
    }

    if opcode in ["0001", "0100", "0010", "0110", "1001"]:
        return op[opcode]
    else:
        return op[opcode] + ", " + operand
