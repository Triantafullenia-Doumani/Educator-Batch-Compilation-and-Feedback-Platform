.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
sw ra, 0(sp)
L1:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -28(sp)
L2:
lw t1, -28(sp)
sw t1, -12(gp)
L3:
lw t1, -12(sp)
lw t2, -16(sp)
bgt t1, t2 L5
L4:
b L9
L5:
lw t1, -12(sp)
lw t2, -20(sp)
bgt t1, t2 L7
L6:
b L9
L7:
lw t1, -12(sp)
sw t1, -24(sp)
L8:
b L16
L9:
lw t1, -16(sp)
lw t2, -12(sp)
bgt t1, t2 L11
L10:
b L15
L11:
lw t1, -16(sp)
lw t2, -20(sp)
bgt t1, t2 L13
L12:
b L15
L13:
lw t1, -16(sp)
sw t1, -24(sp)
L14:
b L16
L15:
lw t1, -20(sp)
sw t1, -24(sp)
L16:
lw t1, -24(sp)
lw t0, -8(sp)
sw t1, 0(t0)
L17:
lw ra, 0(sp)
jr ra
L18:
sw ra, 0(sp)
L19:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
L20:
lw t1, -16(sp)
sw t1, -12(gp)
L21:
lw t1, -12(sp)
li t2, 0
blt t1, t2 L23
L22:
b L25
L23:
li t1, -1
lw t0, -8(sp)
sw t1, 0(t0)
L24:
b L41
L25:
lw t1, -12(sp)
li t2, 0
beq t1, t2 L29
L26:
b L27
L27:
lw t1, -12(sp)
li t2, 1
beq t1, t2 L29
L28:
b L31
L29:
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L30:
b L41
L31:
lw t1, -12(sp)
li t2, 1
sub t1, t1, t2
sw t1, -20(sp)
L32:
addi s0, sp, 40
addi s0, sp, 40
lw t0, -20(sp)
sw t0, -12(s0)
L33:
addi t0, sp, -24
sw t0, -8(s0)
L34:
sw sp, -4(s0)
addi sp, sp, 40
jal L18
addi sp, sp, -40
L35:
lw t1, -12(sp)
li t2, 2
sub t1, t1, t2
sw t1, -28(sp)
L36:
addi s0, sp, 40
lw t0, -28(sp)
sw t0, -12(s0)
L37:
addi t0, sp, -32
sw t0, -8(s0)
L38:
sw sp, -4(s0)
addi sp, sp, 40
jal L18
addi sp, sp, -40
L39:
lw t1, -24(sp)
lw t2, -32(sp)
add t1, t1, t2
sw t1, -36(sp)
L40:
lw t1, -36(sp)
lw t0, -8(sp)
sw t1, 0(t0)
L41:
lw ra, 0(sp)
jr ra
L42:
sw ra, 0(sp)
L43:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
L44:
lw t1, -20(sp)
sw t1, -12(gp)
L45:
lw t1, -16(sp)
lw t2, -12(sp)
div t1, t1, t2
sw t1, -24(sp)
L46:
lw t1, -24(sp)
lw t2, -12(sp)
mul t1, t1, t2
sw t1, -28(sp)
L47:
lw t1, -16(sp)
lw t2, -28(sp)
beq t1, t2 L49
L48:
b L51
L49:
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L50:
b L52
L51:
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)
L52:
lw ra, 0(sp)
jr ra
L53:
sw ra, 0(sp)
L54:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
L55:
lw t1, -20(sp)
sw t1, -12(gp)
L56:
li t1, 2
sw t1, -16(sp)
L57:
lw t1, -16(sp)
lw t2, -12(sp)
blt t1, t2 L59
L58:
b L70
L59:
addi s0, sp, 32
lw t0, -16(sp)
sw t0, -12(s0)
L60:
lw t0, -12(sp)
sw t0, -16(s0)
L61:
addi t0, sp, -24
sw t0, -8(s0)
L62:
sw sp, -4(s0)
addi sp, sp, 32
jal L42
addi sp, sp, -32
L63:
lw t1, -24(sp)
li t2, 1
beq t1, t2 L65
L64:
b L67
L65:
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)
L66:
b L67
L67:
lw t1, -16(sp)
li t2, 1
add t1, t1, t2
sw t1, -28(sp)
L68:
lw t1, -28(sp)
sw t1, -16(sp)
L69:
b L57
L70:
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L71:
lw ra, 0(sp)
jr ra
L72:
sw ra, 0(sp)
L73:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
L74:
lw t1, -16(sp)
sw t1, -12(gp)
L75:
lw t1, -12(sp)
lw t2, -12(sp)
mul t1, t1, t2
sw t1, -20(sp)
L76:
lw t1, -20(sp)
lw t0, -8(sp)
sw t1, 0(t0)
L77:
lw ra, 0(sp)
jr ra
L78:
sw ra, 0(sp)
L79:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -20(sp)
L80:
lw t1, -20(sp)
sw t1, -12(gp)
L81:
addi s0, sp, 24
addi s0, sp, 24
lw t0, -12(sp)
sw t0, -12(s0)
L82:
addi t0, sp, -24
sw t0, -8(s0)
L83:
sw sp, -4(s0)
addi sp, sp, 24
jal L72
addi sp, sp, -24
L84:
addi s0, sp, 24
lw t0, -12(sp)
sw t0, -12(s0)
L85:
addi t0, sp, -28
sw t0, -8(s0)
L86:
sw sp, -4(s0)
addi sp, sp, 24
jal L72
addi sp, sp, -24
L87:
lw t1, -24(sp)
lw t2, -28(sp)
mul t1, t1, t2
sw t1, -32(sp)
L88:
lw t1, -32(sp)
sw t1, -16(sp)
L89:
lw t1, -16(sp)
lw t0, -8(sp)
sw t1, 0(t0)
L90:
lw ra, 0(sp)
jr ra
L91:
sw ra, 0(sp)
L92:
lw t1, -12(gp)
li t2, 1
add t1, t1, t2
sw t1, -16(sp)
L93:
lw t1, -16(sp)
sw t1, -12(gp)
L94:
lw t1, -12(sp)
li t2, 4
rem t1, t1, t2
sw t1, -20(sp)
L95:
lw t1, -20(sp)
li t2, 0
beq t1, t2 L97
L96:
b L100
L97:
lw t1, -12(sp)
li t2, 100
rem t1, t1, t2
sw t1, -24(sp)
L98:
lw t1, -24(sp)
li t2, 0
bne t1, t2 L103
L99:
b L100
L100:
lw t1, -12(sp)
li t2, 400
rem t1, t1, t2
sw t1, -28(sp)
L101:
lw t1, -28(sp)
li t2, 0
beq t1, t2 L103
L102:
b L105
L103:
li t1, 1
lw t0, -8(sp)
sw t1, 0(t0)
L104:
b L106
L105:
li t1, 0
lw t0, -8(sp)
sw t1, 0(t0)
L106:
lw ra, 0(sp)
jr ra
L107:
Lmain:
addi sp, sp, 52
mv gp, sp
L108:
li t1, 0
sw t1, -12(sp)
L109:
li a7, 5
ecall
mv t1, a0
sw t1, -16(sp)
L110:
lw t1, -16(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L111:
li t1, 1600
sw t1, -16(sp)
L112:
lw t1, -16(sp)
li t2, 2000
ble t1, t2 L114
L113:
b L121
L114:
addi s0, sp, 32
addi s0, sp, 32
addi s0, sp, 32
addi s0, sp, 36
addi s0, sp, 40
addi s0, sp, 32
lw t0, -16(sp)
sw t0, -12(s0)
L115:
addi t0, sp, -20
sw t0, -8(s0)
L116:
sw sp, -4(s0)
addi sp, sp, 32
jal L91
addi sp, sp, -32
L117:
lw t1, -20(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L118:
lw t1, -16(sp)
li t2, 400
add t1, t1, t2
sw t1, -24(sp)
L119:
lw t1, -24(sp)
sw t1, -16(sp)
L120:
b L112
L121:
addi s0, sp, 32
addi s0, sp, 32
addi s0, sp, 36
addi s0, sp, 40
addi s0, sp, 32
li t0, 2023
sw t0, -12(s0)
L122:
addi t0, sp, -28
sw t0, -8(s0)
L123:
sw sp, -4(s0)
addi sp, sp, 32
jal L91
addi sp, sp, -32
L124:
lw t1, -28(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L125:
addi s0, sp, 32
addi s0, sp, 36
addi s0, sp, 40
addi s0, sp, 32
li t0, 2024
sw t0, -12(s0)
L126:
addi t0, sp, -32
sw t0, -8(s0)
L127:
sw sp, -4(s0)
addi sp, sp, 32
jal L91
addi sp, sp, -32
L128:
lw t1, -32(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L129:
addi s0, sp, 36
addi s0, sp, 40
addi s0, sp, 32
li t0, 3
sw t0, -12(s0)
L130:
addi t0, sp, -36
sw t0, -8(s0)
L131:
sw sp, -4(s0)
addi sp, sp, 36
jal L78
addi sp, sp, -36
L132:
lw t1, -36(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L133:
addi s0, sp, 40
addi s0, sp, 32
li t0, 5
sw t0, -12(s0)
L134:
addi t0, sp, -40
sw t0, -8(s0)
L135:
sw sp, -4(s0)
addi sp, sp, 40
jal L18
addi sp, sp, -40
L136:
lw t1, -40(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L137:
li t1, 1
sw t1, -16(sp)
L138:
lw t1, -16(sp)
li t2, 12
ble t1, t2 L140
L139:
b L147
L140:
addi s0, sp, 32
lw t0, -16(sp)
sw t0, -12(s0)
L141:
addi t0, sp, -44
sw t0, -8(s0)
L142:
sw sp, -4(s0)
addi sp, sp, 32
jal L53
addi sp, sp, -32
L143:
lw t1, -44(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L144:
lw t1, -16(sp)
li t2, 1
add t1, t1, t2
sw t1, -48(sp)
L145:
lw t1, -48(sp)
sw t1, -16(sp)
L146:
b L138
L147:
lw t1, -12(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L148:
li a0, 0
li a7, 93
ecall
L149:
