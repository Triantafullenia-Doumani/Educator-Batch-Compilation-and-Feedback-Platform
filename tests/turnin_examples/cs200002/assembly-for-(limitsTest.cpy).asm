	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
Lmain:
	sw ra,0(sp)
L2:
	lw t0, -24(sp)
	li a0, 0
	li a2, 1
	li a7,63
	ecall
	mv t0, a0
L3:
	li a0, 0
	li a7, 93
	ecall
L4:
	lw ra,0(sp)
	jr ra
