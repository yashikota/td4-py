"""
emulation TD4
"""

import td4.parse
import td4.output
import td4.opcode

import argparse
import time


class Emulator:
    def __init__(self):
        self.inst = None  # Instruction
        self.pc = 0  # Program Counter
        self.im = list()  # Instruction Memory

        self.reg_a = "0000"  # Register A
        self.reg_b = "0000"  # Register B
        self.c_flag = "0"  # Carry Flag

        self.input = "0000"  # Input
        self.output = "0000"  # Output

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
        match self.opcode:
            case "0011":  # MOV A, Im
                self.reg_a = self.operand
            case "0111":  # MOV B, Im
                self.reg_b = self.operand
            case "0001":  # MOV A, B
                self.reg_a = self.reg_b
            case "0100":  # MOV B, A
                self.reg_b = self.reg_a
            case "0000":  # ADD A, Im
                pass
            case "0101":  # ADD B, Im
                pass
            case "0010":  # IN A
                self.reg_a = self.input
            case "0110":  # IN B
                self.reg_b = self.input
            case "1011":  # OUT Im
                self.output = self.operand
            case "1001":  # OUT B
                self.output = self.reg_b
            case "1111":  # JMP
                self.pc = int(self.operand, 2)
            case "1110":  # JNC
                if self.c_flag == "0":
                    self.pc = int(self.operand, 2)

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
        except KeyError:
            print("Invalid instruction")
            exit(1)

        try:
            while self.pc < len(self.im):
                td4.output.output(
                    self.reg_a,
                    self.reg_b,
                    self.c_flag,
                    self.im,
                    self.pc,
                    self.clk,
                    self.input,
                    self.output,
                    self.beep,
                )

                self.fetch()
                self.decode()
                self.execute()

                self.clock()
        except KeyboardInterrupt:
            print("Finished")
            exit(0)
        except KeyError:
            print("Invalid instruction")
            exit(1)

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
