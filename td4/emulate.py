"""
emulation TD4
"""

import td4.parse
import td4.output

import argparse
import time


class Emulator:
    def __init__(self):
        self.inst = None  # Instruction
        self.pc = 0  # Program Counter
        self.im = list()  # Instruction Memory

    def clock(self):
        if self.clk.isnumeric():
            interval = 1 / int(self.clk)
            time.sleep(interval)
        elif self.clk == "manual":
            input()

    def fetch(self):
        self.inst = self.im[self.pc]
        self.pc += 1

    def decode(self):
        self.opcode = self.inst[:4]
        self.operand = self.inst[4:]

    def execute(self):
        pass

    def emulator(self):
        args = self.arg_parse()
        self.file = args.file
        self.input = args.input
        self.clk = args.clock
        self.beep = args.beep

        try:
            with open(self.file, "r") as file:
                if file.name.endswith(".td4"):
                    self.im, self.clk, self.beep = td4.parse.to_binary_td4(
                        file.read().splitlines()
                    )
                else:
                    self.im = [
                        td4.parse.to_binary(line) for line in file.read().splitlines()
                    ]
            if len(self.im) > 16:
                raise ValueError
        except FileNotFoundError:
            print("File not found")
            exit(1)
        except ValueError:
            print("Too many instructions\nTD4 can only handle 16 instructions")
            exit(1)
        else:
            while self.pc < len(self.im):
                td4.output.output(self.im, self.pc, self.clk, self.input, self.beep)
                self.fetch()
                self.decode()
                self.execute()

                self.clock()

    def arg_parse(self):
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
