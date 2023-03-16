import sys

import td4


def main():
    if len(sys.argv) > 1:
        print("Read from file")
        try:
            with open(sys.argv[1], "r") as f:
                enter = f.read().splitlines()
        except FileNotFoundError:
            print("File not found")
            exit(1)
    else:
        print("Input from stdin. Ctrl + D to end.")
        enter = sys.stdin.read().splitlines()

    td4.emulator(enter)


if __name__ == "__main__":
    main()
