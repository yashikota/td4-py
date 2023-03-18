import td4.parse


def output(im, pc, clock, input, beep):
    print("\033[2J\033[1;1H", end="")

    print("=== TD4 Emulator ===")
    print(f"Reg A\t: 0000")
    print(f"Reg B\t: 0000")
    print(f"C Flag\t: 0")
    print(f"PC\t: {pc}")

    print()
    if clock.isnumeric():
        print(f"Clock\t: {clock}Hz")
    elif clock == "manual":
        print("Clock\t: manual")
    print(f"Input\t: {input}")
    print(f"Output\t: ● ○ ○ ○")
    print(f"Beep\t: {beep}")
    print("=== Instruction Memory ===")
    for i, inst in enumerate(im):
        if i == pc:
            print(
                "\033[1;31m[{0:2d}] {1:<11} ({2} {3})\033[0m".format(
                    i, td4.parse.to_assembly(inst), inst[:4], inst[4:]
                )
            )
        else:
            print(
                "[{0:2d}] {1:<11} ({2} {3})".format(
                    i, td4.parse.to_assembly(inst), inst[:4], inst[4:]
                )
            )
    print("=====================")
