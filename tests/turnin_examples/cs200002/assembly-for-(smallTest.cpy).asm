	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
	sw ra,0(sp)
L2:
	li t0, 1
L3:
	lw t0, -36(gp)
L4:
	lw t0, -16(gp)
L5:
	lw t0 -8(sp)
	lw t1, -48(sp)
	sw t1, 0(t0)
L6:
	lw ra,0(sp)
	jr ra
L7:
	sw ra,0(sp)
L8:
	lw t0, -32(gp)
L9:
	addi s0,sp,0
L10:
	lw t0, -32(gp)
	sw t0, -32(s0)
L11:
	addi t0, sp, -32
	sw t0, -8(s0)
L12:
	jal ra, L1
L13:
	lw t0, -56(sp)
L14:
	addi s0,sp,0
L15:
	lw t0, -32(gp)
	sw t0, -32(s0)
L16:
	lw t0, -36(gp)
	sw t0, -36(s0)
L17:
	addi t0, sp, -36
	sw t0, -8(s0)
L18:
	jal ra, L7
L19:
	lw t0, -68(sp)
L20:
	lw t0, -16(gp)
L21:
	lw t0 -8(sp)
	lw t1, -28(sp)
	sw t1, 0(t0)
L22:
	lw ra,0(sp)
	jr ra
L23:
Lmain:
	sw ra,0(sp)
L24:
	lw t0, -16(gp)
	li t1, 1
L25:
	j L27
L26:
	lw t0, -24(gp)
	li t1, 2
	bge t0, t1, L31
L27:
	j L27
L28:
	lw t0, -20(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -36(sp)
L29:
	lw t0, -24(gp)
	lw t1, -16(gp)
	add t0, t1, t2
	sw t2, -40(sp)
L30:
	lw t0, -36(sp)
	lw t1, -40(sp)
	bge t0, t1, L31
L31:
	j L37
L32:
	addi s0,sp,-1
L33:
	lw t0, -20(gp)
	sw t0, -20(s0)
L34:
	lw t0, -16(gp)
	sw t0, -16(s0)
L35:
	addi t0, sp, -16
	sw t0, -8(s0)
L36:
	jal ra, L7
L37:
	lw t0, -52(sp)
L38:
	j L38
L39:
	li t0, 1
L40:
	li a0, 0
	li a7, 93
	ecall
L41:
	lw ra,0(sp)
	jr ra
