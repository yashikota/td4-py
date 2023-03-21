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
    # Initialize
    pc = 0  # Program Counter
    reg_a = "0000"  # Register A
    reg_b = "0000"  # Register B
    c_flag = "0"  # Carry Flag
    output = "0000"  # Output

    # Parse arguments
    args = arg_parse()
    file = args.file
    input = args.input
    clk = args.clock
    beep = args.beep

    # Check input
    try:
        if len(input) != 4 or not input.isnumeric() or int(input, 2) > 15:
            raise ValueError
    except ValueError:
        print("Invalid input")
        exit(1)

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
        td4.output.output(reg_a, reg_b, c_flag, rom, pc, clk, input, output, beep)
        while pc < len(rom):
            inst, pc = td4.cpu.fetch(rom, pc)
            op, im = td4.cpu.decode(inst)
            reg_a, reg_b, c_flag, output, pc = td4.cpu.execute(
                op, im, reg_a, reg_b, c_flag, input, output, pc
            )
            if beep and output[0] == "1":
                print("\a")
            clock(clk)
            td4.output.output(reg_a, reg_b, c_flag, rom, pc, clk, input, output, beep)
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
    url = "https://github.com/yashikota/td4-py#support-file-format"
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help=f"File to read\nCheck {url} for the supported format.",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--input",
        help="Default 0000. Any binary can be specified.",
        type=str,
        default="0000",
    )
    parser.add_argument(
        "-c",
        "--clock",
        help="Default 10Hz. Any number and manual can be specified.",
        type=str,
        default="10",
    )
    parser.add_argument("-b", "--beep", help="Default False.", action="store_true")
    args = parser.parse_args()

    return args
