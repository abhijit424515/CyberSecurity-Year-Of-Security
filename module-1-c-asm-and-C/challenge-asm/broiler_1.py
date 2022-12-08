from pwn import *

context.arch = "amd64"
context.log_level= "INFO"
context.encoding = "latin"
warnings.simplefilter("ignore")

chall = os.path.basename(__file__).split('_')[1].split('.')[0]
level = 4   #mention level: [1,5]

""""write your assembly code below"""
assembly = """
mov qword ptr [rdi], 0xdead
mov qword ptr [rsi], 0x0000
"""

with process(['python3', f'chall_{chall}.py', str(level)]) as p:
    info(p.readrepeat(1))
    p.send(asm(assembly))
    info(p.readrepeat(1))

