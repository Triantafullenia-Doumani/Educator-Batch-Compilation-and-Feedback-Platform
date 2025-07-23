	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
Lmain:
	sw ra,0(sp)
L2:
	li t0, 1
L3:
	li t0, 2
L4:
	lw t0, -20(gp)
	lw t1, -24(gp)
	add t0, t1, t2
	sw t2, -36(sp)
L5:
	lw t0, -36(sp)
	li t1, 1
	bge t0, t1, L8
L6:
	j L30
L7:
	lw t0, -24(gp)
	li t1, 5
	bge t0, t1, L10
L8:
	j L30
L9:
	lw t0, -28(gp)
	li t1, 1
L10:
	j L14
L11:
	li t0, 2
L12:
	j L19
L13:
	lw t0, -28(gp)
	li t1, 2
L14:
	j L18
L15:
	li t0, 4
L16:
	j L19
L17:
	li t0, 0
L18:
	lw t0, -20(gp)
	li t1, 1
	bge t0, t1, L21
L19:
	j L29
L20:
	lw t0, -20(gp)
	li t1, 2
L21:
	j L28
L22:
	lw t0, -24(gp)
	li t1, 1
L23:
	j L27
L24:
	li t0, 2
L25:
	j L23
L26:
	j L28
L27:
	j L19
L28:
	j L5
L29:
	li a0, 0
	li a7, 93
	ecall
L30:
	lw ra,0(sp)
	jr ra
