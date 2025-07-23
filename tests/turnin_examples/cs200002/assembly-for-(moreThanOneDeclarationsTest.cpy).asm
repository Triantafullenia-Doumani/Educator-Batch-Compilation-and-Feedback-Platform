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
	lw t0, -32(sp)
	li a0, 0
	li a2, 1
	li a7,63
	ecall
	mv t0, a0
L4:
	lw t0, -32(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L5:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L6:
	li a0, 0
	li a7, 93
	ecall
L7:
	lw ra,0(sp)
	jr ra
