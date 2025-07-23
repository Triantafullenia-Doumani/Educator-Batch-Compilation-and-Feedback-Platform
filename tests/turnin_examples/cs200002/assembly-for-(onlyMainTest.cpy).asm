	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
Lmain:
	sw ra,0(sp)
L2:
	li t0, 0
L3:
	lw t0, -24(sp)
	li a0, 0
	li a2, 1
	li a7,63
	ecall
	mv t0, a0
L4:
	lw t0, -24(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L5:
	li t0, 1600
	sw t0, -24(sp)
L6:
	lw t0, -24(sp)
	li t1, 2000
L7:
	j L12
L8:
	lw t0, -24(sp)
	addi t1, zero, 400
	add t0, t1, t2
	sw t2, -32(sp)
L9:
	lw t0, -32(sp)
	sw t0, -24(sp)
L10:
	j L7
L11:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L12:
	li a0, 0
	li a7, 93
	ecall
L13:
	lw ra,0(sp)
	jr ra
