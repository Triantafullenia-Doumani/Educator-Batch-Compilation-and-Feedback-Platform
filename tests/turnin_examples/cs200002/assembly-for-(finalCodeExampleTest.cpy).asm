	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
	sw ra,0(sp)
L2:
	li t0, 4
	sw t0, -52(sp)
L3:
	lw t0, -20(gp)
L4:
	lw t0, -32(gp)
L5:
	lw t0, -4(sp)
	addi t0, t0, 40
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t1, -52(sp)
	add t0, t1, t2
	sw t2, -56(sp)
L6:
	lw t0 -8(sp)
	lw t1, -44(sp)
	sw t1, 0(t0)
L7:
	lw ra,0(sp)
	jr ra
L8:
	sw ra,0(sp)
L9:
	li t0, 3
L10:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L11:
	lw t0, -20(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L12:
	addi s0,sp,0
L13:
	li t0, 2
	sw t0, -48(s0)
L14:
	addi t0, sp, -48
	sw t0, -8(s0)
L15:
	jal ra, L1
L16:
	lw t0, -52(sp)
L17:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L18:
	lw t0, -20(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L19:
	lw t0 -8(sp)
	lw t1, -28(sp)
	sw t1, 0(t0)
L20:
	lw ra,0(sp)
	jr ra
L21:
Lmain:
	sw ra,0(sp)
L22:
	li t0, 1
L23:
	li t0, 2
L24:
	addi s0,sp,-1
L25:
	lw t0, -16(gp)
	sw t0, -16(s0)
L26:
	lw t0, -20(gp)
	sw t0, -20(s0)
L27:
	addi t0, sp, -20
	sw t0, -8(s0)
L28:
	jal ra, L8
L29:
	lw t0, -44(sp)
L30:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L31:
	lw t0, -20(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L32:
	lw t0, -24(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L33:
	li a0, 0
	li a7, 93
	ecall
L34:
	lw ra,0(sp)
	jr ra
