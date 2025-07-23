


L1:
sw ra,(sp)
addi sp, sp, -4
L2:
li t1,2023
sw t1,-12(sp)
L3:
lw t1,-12(sp)
addi a0,t1, 0
li a7,1
ecall
L4:
li a7,5
ecall
addi t1,a0, 0
sw t1,-16(sp)
L5:
lw t1,-16(sp)
li t2,1
add t1,t1,t2
sw t1,-20(sp)
L6:
lw t1,-20(sp)
sw t1,-16(sp)
L7:
lw t1,-16(sp)
addi a0,t1, 0
li a7,1
ecall
L8:
lw ra,(sp)
addi sp, sp, 4
jr ra
