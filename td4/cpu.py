def fetch(rom, pc):
    return rom[pc], pc + 1


def decode(inst):
    return inst[:4], inst[4:]


def execute(op, im, reg_a, reg_b, c_flag, input, output, pc):
    match op:
        case "0011":  # MOV A, Im
            reg_a = im
            c_flag = "0"
        case "0111":  # MOV B, Im
            reg_b = im
            c_flag = "0"
        case "0001":  # MOV A, B
            reg_a = reg_b
            c_flag = "0"
        case "0100":  # MOV B, A
            reg_b = reg_a
            c_flag = "0"
        case "0000":  # ADD A, Im
            reg_a, c_flag = add(reg_a, im)
        case "0101":  # ADD B, Im
            reg_b, c_flag = add(reg_b, im)
        case "0010":  # IN A
            reg_a = input
            c_flag = "0"
        case "0110":  # IN B
            reg_b = input
            c_flag = "0"
        case "1011":  # OUT Im
            output = im
            c_flag = "0"
        case "1001":  # OUT B
            output = reg_b
            c_flag = "0"
        case "1111":  # JMP
            pc = int(im, 2)
            c_flag = "0"
        case "1110":  # JNC
            if c_flag == "0":
                pc = int(im, 2)

    return reg_a, reg_b, c_flag, output, pc


def add(reg, im):
    result = bin(int(reg, 2) + int(im, 2))[2:].zfill(4)
    if len(result) > 4:
        c_flag = "1"
        result = result[1:]
    else:
        c_flag = "0"
    return result, c_flag
