	.data
	str_nl: .asciz "\n"
	.text
L0:
	j Lmain
L1:
	sw ra,0(sp)
L2:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -44(sp)
L3:
	lw t0, -44(sp)
L4:
	lw t0, -24(gp)
	lw t1, -28(gp)
L5:
	j L11
L6:
	lw t0, -24(gp)
	lw t1, -32(gp)
L7:
	j L11
L8:
	lw t0, -24(gp)
	sw t0, -36(sp)
L9:
	j L18
L10:
	lw t0, -28(gp)
	lw t1, -24(gp)
L11:
	j L17
L12:
	lw t0, -28(gp)
	lw t1, -32(gp)
L13:
	j L17
L14:
	lw t0, -28(gp)
	sw t0, -36(sp)
L15:
	j L18
L16:
	lw t0, -32(gp)
	sw t0, -36(sp)
L17:
	lw t0 -8(sp)
	lw t1, -20(sp)
	sw t1, 0(t0)
L18:
	lw ra,0(sp)
	jr ra
L19:
	sw ra,0(sp)
L20:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -36(sp)
L21:
	lw t0, -36(sp)
L22:
	lw t0, -24(gp)
	li t1, 0
	bge t0, t1, L25
L23:
	j L28
L24:
	addi t0, zero, 0
	addi t1, zero, 1
	sub t0, t1, t2
	sw t2, -40(sp)
L25:
	lw t0 -8(sp)
	lw t1, -24(sp)
	sw t1, 0(t0)
L26:
	j L44
L27:
	lw t0, -24(gp)
	li t1, 0
L28:
	j L30
L29:
	lw t0, -24(gp)
	li t1, 1
L30:
	j L34
L31:
	lw t0 -8(sp)
	lw t1, -24(sp)
	sw t1, 0(t0)
L32:
	j L44
L33:
	lw t0, -24(gp)
	addi t1, zero, 1
	sub t0, t1, t2
	sw t2, -44(sp)
L34:
	addi s0,sp,0
L35:
	lw t0, -44(sp)
	sw t0, -44(s0)
L36:
	addi t0, sp, -44
	sw t0, -8(s0)
L37:
	jal ra, L19
L38:
	lw t0, -24(gp)
	addi t1, zero, 2
	sub t0, t1, t2
	sw t2, -56(sp)
L39:
	addi s0,sp,0
L40:
	lw t0, -56(sp)
	sw t0, -56(s0)
L41:
	addi t0, sp, -56
	sw t0, -8(s0)
L42:
	jal ra, L19
L43:
	lw t0, -52(sp)
	lw t1, -64(sp)
	add t0, t1, t2
	sw t2, -68(sp)
L44:
	lw t0 -8(sp)
	lw t1, -24(sp)
	sw t1, 0(t0)
L45:
	lw ra,0(sp)
	jr ra
L46:
	sw ra,0(sp)
L47:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -56(sp)
L48:
	lw t0, -56(sp)
L49:
	lw t0, -28(gp)
	lw t1, -24(gp)
	div t0, t1, t2
	sw t2, -60(sp)
L50:
	lw t0, -60(sp)
	lw t1, -24(gp)
	mul t0, t1, t2
	sw t2, -64(sp)
L51:
	lw t0, -28(gp)
	lw t1, -64(sp)
L52:
	j L54
L53:
	lw t0 -8(sp)
	lw t1, -40(sp)
	sw t1, 0(t0)
L54:
	j L55
L55:
	lw t0 -8(sp)
	lw t1, -40(sp)
	sw t1, 0(t0)
L56:
	lw ra,0(sp)
	jr ra
L57:
	sw ra,0(sp)
L58:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -48(sp)
L59:
	lw t0, -48(sp)
L60:
	li t0, 2
L61:
	lw t0, -4(sp)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t1, -24(gp)
	bge t0, t1, L62
L62:
	j L73
L63:
	addi s0,sp,0
L64:
	lw t0, -4(sp)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	sw t0, -36(s0)
L65:
	lw t0, -24(gp)
	sw t0, -24(s0)
L66:
	addi t0, sp, -24
	sw t0, -8(s0)
L67:
	jal ra, L46
L68:
	lw t0, -60(sp)
	li t1, 1
L69:
	j L70
L70:
	lw t0 -8(sp)
	lw t1, -28(sp)
	sw t1, 0(t0)
L71:
	j L70
L72:
	lw t0, -4(sp)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -64(sp)
L73:
	lw t0, -64(sp)
L74:
	j L60
L75:
	lw t0 -8(sp)
	lw t1, -28(sp)
	sw t1, 0(t0)
L76:
	lw ra,0(sp)
	jr ra
L77:
	sw ra,0(sp)
L78:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -56(sp)
L79:
	lw t0, -56(sp)
L80:
	lw t0, -24(gp)
	lw t1, -24(gp)
	mul t0, t1, t2
	sw t2, -60(sp)
L81:
	lw t0 -8(sp)
	lw t1, -44(sp)
	sw t1, 0(t0)
L82:
	lw ra,0(sp)
	jr ra
L83:
	sw ra,0(sp)
L84:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -52(sp)
L85:
	lw t0, -52(sp)
L86:
	addi s0,sp,0
L87:
	lw t0, -24(gp)
	sw t0, -24(s0)
L88:
	addi t0, sp, -24
	sw t0, -8(s0)
L89:
	jal ra, L77
L90:
	addi s0,sp,0
L91:
	lw t0, -24(gp)
	sw t0, -24(s0)
L92:
	addi t0, sp, -24
	sw t0, -8(s0)
L93:
	jal ra, L77
L94:
	lw t0, -60(sp)
	lw t1, -68(sp)
	mul t0, t1, t2
	sw t2, -72(sp)
L95:
	lw t0, -72(sp)
L96:
	lw t0 -8(sp)
	lw t1, -32(sp)
	sw t1, 0(t0)
L97:
	lw ra,0(sp)
	jr ra
L98:
	sw ra,0(sp)
L99:
	lw t0, -16(gp)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -48(sp)
L100:
	lw t0, -48(sp)
L101:
	lw t0, -4(sp)
	addi t0, t0, 40
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t1, 4
	lw t2, -52(sp)
	rem t2,t0,t1
	sw t2, -52(sp)
L102:
	lw t0, -52(sp)
	li t1, 0
L103:
	j L103
L104:
	lw t0, -4(sp)
	addi t0, t0, 40
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t1, 100
	lw t2, -56(sp)
	rem t2,t0,t1
	sw t2, -56(sp)
L105:
	lw t0, -56(sp)
	li t1, 0
	bne t0, t1, L106
L106:
	j L103
L107:
	lw t0, -4(sp)
	addi t0, t0, 40
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t1, 400
	lw t2, -60(sp)
	rem t2,t0,t1
	sw t2, -60(sp)
L108:
	lw t0, -60(sp)
	li t1, 0
L109:
	j L108
L110:
	lw t0 -8(sp)
	lw t1, -36(sp)
	sw t1, 0(t0)
L111:
	j L109
L112:
	lw t0 -8(sp)
	lw t1, -36(sp)
	sw t1, 0(t0)
L113:
	lw ra,0(sp)
	jr ra
L114:
Lmain:
	sw ra,0(sp)
L115:
	li t0, 0
L116:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	li a0, 0
	li a2, 1
	li a7,63
	ecall
	mv t0, a0
L117:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw a0, 0(t0)
	li a7,1
	ecall
L118:
	li t0, 1600
L119:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t1, 2000
L120:
	j L124
L121:
	addi s0,sp,-1
L122:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	sw t0, -36(s0)
L123:
	addi t0, sp, -36
	sw t0, -8(s0)
L124:
	jal ra, L98
L125:
	lw t0, -52(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L126:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	addi t1, zero, 400
	add t0, t1, t2
	sw t2, -56(sp)
L127:
	lw t0, -56(sp)
L128:
	j L115
L129:
	addi s0,sp,-1
L130:
	li t0, 2023
	sw t0, -60(s0)
L131:
	addi t0, sp, -60
	sw t0, -8(s0)
L132:
	jal ra, L98
L133:
	lw t0, -64(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L134:
	addi s0,sp,-1
L135:
	li t0, 2024
	sw t0, -68(s0)
L136:
	addi t0, sp, -68
	sw t0, -8(s0)
L137:
	jal ra, L98
L138:
	lw t0, -72(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L139:
	addi s0,sp,-1
L140:
	li t0, 3
	sw t0, -76(s0)
L141:
	addi t0, sp, -76
	sw t0, -8(s0)
L142:
	jal ra, L83
L143:
	lw t0, -80(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L144:
	addi s0,sp,-1
L145:
	li t0, 5
	sw t0, -84(s0)
L146:
	addi t0, sp, -84
	sw t0, -8(s0)
L147:
	jal ra, L19
L148:
	lw t0, -88(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L149:
	li t0, 1
L150:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t1, 12
L151:
	j L150
L152:
	addi s0,sp,-1
L153:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	sw t0, -36(s0)
L154:
	addi t0, sp, -36
	sw t0, -8(s0)
L155:
	jal ra, L57
L156:
	lw t0, -96(sp)
	lw a0, 0(t0)
	li a7,1
	ecall
L157:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	lw t0, -4(t0)
	addi t0, t0, 36
	lw t0, 0(t0)
	lw t1, 0(t0)
	addi t1, zero, 1
	add t0, t1, t2
	sw t2, -100(sp)
L158:
	lw t0, -100(sp)
L159:
	j L141
L160:
	lw t0, -16(gp)
	lw a0, 0(t0)
	li a7,1
	ecall
L161:
	li a0, 0
	li a7, 93
	ecall
L162:
	lw ra,0(sp)
	jr ra
