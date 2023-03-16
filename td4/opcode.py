"""
instruction set
"""


def opcode(arg):
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
