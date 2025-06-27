.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
	sw ra,(sp)
L1:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	sw t1, -20(sp)
L2:
	lw t1, -20(sp)
	sw t1, -16(sp)
L3:
	lw t1, -16(sp)
	lw t2, -12(sp)
	add t1, t1, t2
	sw t1, -24(sp)
L4:
	lw t1, -24(sp)
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, (t0)
L5:
	lw a0, -16(sp)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L6:
	lw t0, -8(sp)
	lw t1, -16(sp)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 28
	jr ra
L7:
	lw ra, 0(sp)
	addi sp, sp, 28
	jr ra
Lmain:
	addi sp, sp, -16
	mv fp, sp
L8:
	li a7, 5
	ecall
	add t1, zero, a0
	sw t1, -12(sp)
	lw t0, -4(sp)
	addi t0, t0, -12
	sw a0, (t0)
L9:
L10:
L11:
	addi fp, sp, -28
	lw t0, -12(sp)
	sw t0, -12(fp)
L12:
	addi t0, sp, -12
	sw t0, -8(fp)
L13:
	sw sp, -4(fp)
	addi sp, sp, -28
	jal L0
	addi sp, sp, 28
L14:
L15:
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, (t0)
L16:
	lw a0, -16(sp)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L17:
	li a0, 0
	li a7, 93
	ecall
