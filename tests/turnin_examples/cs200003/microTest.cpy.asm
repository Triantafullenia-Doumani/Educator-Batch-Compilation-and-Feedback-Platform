.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
Lmain:
addi sp, sp, 36
mv gp, sp
L1:
li t1, 0
sw t1, -12(sp)
L2:
li t1, 4
sw t1, -16(sp)
L3:
lw t1, -12(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L4:
lw t1, -16(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L5:
lw t1, -16(sp)
li t2, 2
add t1, t1, t2
sw t1, -20(sp)
L6:
lw t1, -20(sp)
sw t1, -16(sp)
L7:
lw t1, -16(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L8:
lw t1, -16(sp)
li t2, 3
mul t1, t1, t2
sw t1, -24(sp)
L9:
lw t1, -24(sp)
li t2, 5
sub t1, t1, t2
sw t1, -28(sp)
L10:
lw t1, -28(sp)
sw t1, -12(sp)
L11:
lw t1, -12(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L12:
lw t1, -12(sp)
li t2, 3
rem t1, t1, t2
sw t1, -32(sp)
L13:
lw t1, -32(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L14:
li a0, 0
li a7, 93
ecall
L15:
