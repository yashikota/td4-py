"""
emulation TD4
"""

import td4.cpu
import td4.output
import td4.opcode
import td4.parse

import argparse
import time


def emulator():
    # Parse arguments
    args = arg_parse()
    file = args.file
    input = args.input
    clk = args.clock
    beep = args.beep

    # Initialize
    pc = 0  # Program Counter
    rom = list()  # ROM
    reg_a = "0000"  # Register A
    reg_b = "0000"  # Register B
    c_flag = "0"  # Carry Flag
    input = "0000"  # Input
    output = "0000"  # Output

    # Read file
    try:
        with open(file, "r") as file:
            if file.name.endswith(".td4"):
                rom, clk, beep = td4.parse.to_binary_td4(file.read().splitlines())
            else:
                rom = [td4.parse.to_binary(line) for line in file.read().splitlines()]
        if len(rom) > 16:
            raise ValueError
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except ValueError:
        print("Too many instructions\nTD4 can only handle 16 instructions")
        exit(1)
    except KeyError:
        print("Invalid instruction")
        exit(1)

    # Emulate
    try:
        while pc < len(rom):
            td4.output.output(reg_a, reg_b, c_flag, rom, pc, clk, input, output, beep)
            inst, pc = td4.cpu.fetch(rom, pc)
            op, im = td4.cpu.decode(inst)
            reg_a, reg_b, c_flag, output, pc = td4.cpu.execute(
                op, im, reg_a, reg_b, c_flag, input, output, pc
            )
            clock(clk)
    except KeyboardInterrupt:
        print("Finished")
        exit(0)
    except KeyError:
        print("Invalid instruction")
        exit(1)


def clock(clk):
    if clk.isnumeric():
        interval = 1 / int(clk)
        time.sleep(interval)
    elif clk == "manual":
        input()


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="File to read\nCheck https://github.com/yashikota/td4-py#support-file-format for the supported format.",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--input",
        help="Input\nDefault 0000.\nAny number can be specified.",
        type=str,
        default="0000",
    )
    parser.add_argument(
        "-c",
        "--clock",
        help="Clock speed\nDefault 10Hz.\nAny number and manual can be specified.",
        type=str,
        default="10",
    )
    parser.add_argument(
        "-b", "--beep", help="Beep\nDefault False.", action="store_true"
    )
    args = parser.parse_args()

    return args
