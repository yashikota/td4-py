import td4.parse


def output(reg_a, reg_b, c_flag, im, pc, clock, input, output, beep):
    print("\033[2J\033[1;1H", end="")

    print("=== TD4 Emulator ===")
    print(f"Reg A\t: {reg_a}")
    print(f"Reg B\t: {reg_b}")
    print(f"C Flag\t: {c_flag}")
    print(f"PC\t: {pc}")

    print()
    if clock.isnumeric():
        print(f"Clock\t: {clock}Hz")
    elif clock == "manual":
        print("Clock\t: manual")
    print(f"Input\t: {input}")
    print(f"Output\t: {output} ({to_led(output)})")
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


def to_led(output):
    return "".join([" ●" if output[i] == "1" else " ○" for i in range(4)]).lstrip()
