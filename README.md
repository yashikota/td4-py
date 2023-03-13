# td4-py

This repository is a 4bit CPU emulator written by Python.  
The original is [CPUの創りかた](https://book.mynavi.jp/ec/products/detail/id=22065).  

## features

- Input/output from plain text or td4 format files

## How to run

Supports the input of files in plain text or td4 format and from stdin.  

### Input from files  

plain text.  

```sh
python3 main.py program.txt
```

td4 format text.  

```sh
python3 main.py Knight2K.td4
```

### Input from stdin  

```sh
python3 main.py
```

## File format

It also supports several patterns of input from plain text and stdin.  

### Pattern 1

Opcode(LowerCase) + Space + Operand  

```txt
out 0011
out 0110
out 1100
out 1000
out 1000
out 1100
out 0110
out 0011
out 0001
jmp 0000
```

### Pattern2

Opcode(UpperCase) + Space + Operand  

```txt
OUT 0111
ADD A,0001
JNC 0111
ADD A,0001
JNC 0011
OUT 0110
ADD A,0001
JNC 0110
ADD A,0001
JNC 1000
OUT 0000
OUT 0100
ADD 0001
JNC 1010
OUT 1000
JMP 1111
```

### Pattern3

Opcode(binary) + Operand  

```txt
10110011
10110110
10111100
10111000
10111000
10111100
10110110
10110011
10110001
10010000
```

### Pattern4

Opcode(binary) + Space + Operand  

```txt
1011 0011
1011 0110
1011 1100
1011 1000
1011 1000
1011 1100
1011 0110
1011 0011
1011 0001
1001 0000
```
