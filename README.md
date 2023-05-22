# td4-py

This repository is a 4bit CPU emulator written by Python.  
The original is [CPUの創りかた](https://book.mynavi.jp/ec/products/detail/id=22065).  

## example

### LED

![led](https://raw.githubusercontent.com/yashikota/td4-py/master/img/led.gif)  

### Ramen Timer(x10)

![ramen](https://raw.githubusercontent.com/yashikota/td4-py/master/img/ramen.gif)

## features

- Read from plain text files, td4 format files
- Variable clock, manual clock selectable
- Beep support
- Runs in CLI

## Install

<https://pypi.org/project/td4>  

```sh
pip3 install td4
```

## Usage

### args

```sh
td4 [-h] [-i INPUT] [-c CLOCK] [-b] file
```

#### file

File to read.  
Check https://github.com/yashikota/td4-py#support-file-format for the supported format.  

##### example
.
`td4 program.txt`  
`td4 Knight2K.td4`  

#### help

Show help message and exit.  

##### example

`td4 -h`  

#### input

Any binary can be specified.  
Default is `0000`.  

##### example

`td4 -i 0000`  
`td4 --input 1111`  

#### clock

Any number or manual can be specified.  
Default is `10`.  

##### example

`td4 -c 1`  
`td4 --clock 10`  
`td4 -c manual`  

#### beep

Specifies whether a beep is sounded.  
Operates when the MSB of out is set to 1.  
Default is `False`.  

##### example

`td4 -b`  
`td4 --beep`  

## Support file format

Input from plain text files supports several patterns.  

### Pattern 1

Opcode(Assembly LowerCase) + Space + Immediate data

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

Opcode(Assembly UpperCase) + Space + Immediate data  

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

Opcode(binary) + Immediate data  

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

Opcode(binary) + Space + Immediate data  

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
