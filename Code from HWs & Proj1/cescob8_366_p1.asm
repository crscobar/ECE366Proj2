# Author: Chris Escobar
# ECE 366 Fall 2019 Project 1
# Multiply and Fold hash function


#Part A


# $8 = B = 0xFA19E366
# $9 = A (1-100)
# $10 = addr
# $11 = loopCount (100)
# $12 = C
# $13 = MultFold Couter
# $14 = temp1
# $15 = temp2
# $16 = temp3
# $17 = Ax
# $18 = largest C
# $19
# $20 = div4loop
# $21
# $22
# $23 

lui $8, 0xDE8A
ori $8, $8, 0xAB39


addi $9, $0, 1
ori $10, $0, 0x2020
addi $11, $0, 100
addi $13, $0, 5

loop_100:

	addi $17, $9, 0

	loop_MF:
		multu $17, $8
		mfhi $15
		mflo $14
		xor $17, $15, $14
		addi $13, $13, -1
	bne $13, $0, loop_MF

	addi $16, $17, 0	# $16 = Ax
	srl $16, $16, 16	# A5[31:16]
	sll $17, $17, 16
	srl $17, $17, 16	# A5[15:0]
	xor $12, $16, $17	# C = A5[31:16] XOR A5[15:0]

	addi $16, $12, 0	# $16 = C
	srl $16, $16, 8		# C[15:8]
	sll $12, $12, 24
	srl $12, $12, 24	# C[7:0]
	xor $12, $16, $12	# C = C[15:8] XOR C[7:0]

	sb $12, 0($10)		# Store C in memory

	addi $13, $0, 5		# reset MF loop counter
	addi $9, $9, 1		# increment A
	addi $10, $10, 1	# increment address
	addi $11, $11, -1	# increment 100 loop counter

bne $11, $0, loop_100



# Part B(i)

# $8 = highest
# $9 = 100 loop counter down
# $10 = addr
# $11 = highest addr
# $12
# $13
# $14
# $15 = 4 check loop
# $16 = 4 divide result
# $17 = slt
# $18 = srl/sll
# $19 = final addr
# $20 = final addr addr
# $21
# $22
# $23 

addi $9, $0, 100
addi $15, $0, 2
ori $19, $0, 0x2000
ori $20, $0, 0x2004
ori $10, $0, 0x2020
lbu $8, 0($10)
ori $10, $0, 0x2021

loop_2:
	lbu $18, 0($10)

	slt $17, $18, $8	#if new bit($18) < highest($8), then $17=1
	bne $17, $0, skip	#skips if $17 != 0

	addi $8, $18, 0
	addi $11, $10, 0

	skip:
	addi $9, $9, -1		# increment 100 loop counter
	addi $15, $15, 1
	addi $10, $10, 1
	bne $9, $0, loop_2

sb $8, 0($19)
sb $11, 0($20)
srl $11, $11, 8
addi $20, $20, 1
sb $11, 0($20)



#Part B(ii)

# $8
# $9 = 100 loop counter
# $10 = addr looper
# $11 = 1 and check bit
# $12 = lbu loop
# $13 = mfhi temp
# $14 = ori temp
# $15 = continuous keeper
# $16 = sll/srl and bit
# $17 = loop_bit counter
# $18 = loop_bit checker
# $19 = and result
# $20 = beq 5
# $21 = 5 const
# $22
# $23 = total 11111 count


ori $10, $0, 0x2020
addi $9, $0, 100
addi $11, $0, 1
addi $13, $0, 255
addi $18, $0, 8
addi $17, $0, 0
addi $21, $0, 5

loop_bii:

	lbu $12, 0($10)
	
	loop_bit:
		addi $16, $12, 0
		
		multu $17, $18
		mflo $13
		
		ori $14, $0, 0
		beq $13, $14, first_bit
		
		ori $14, $0, 8
		beq $13, $14, second_bit
		
		ori $14, $0, 16
		beq $13, $14, third_bit
		
		ori $14, $0, 24
		beq $13, $14, fourth_bit
		
		ori $14, $0, 32
		beq $13, $14, fifth_bit
		
		ori $14, $0, 40
		beq $13, $14, sixth_bit
		
		ori $14, $0, 48
		beq $13, $14, seventh_bit
		
		ori $14, $0, 56
		beq $13, $14, eighth_bit
				
		first_bit:
			sll $16, $16, 31	# 1
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		second_bit:
			sll $16, $16, 30	# 2
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		third_bit:
			sll $16, $16, 29	# 3
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		fourth_bit:
			sll $16, $16, 28	# 4
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		fifth_bit:
			sll $16, $16, 27	# 5
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		sixth_bit:
			sll $16, $16, 26	# 6
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		seventh_bit:
			sll $16, $16, 25	# 7
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		eighth_bit:
			sll $16, $16, 24	# 8
			srl $16, $16, 31
			and $19, $16, $11
		beq $0, $0 end_check
		
		end_check:
		beq $19, $0, not_consec
		addi $15, $15, 1
		
		not_consec:
		beq $15, $21, oneoneone
		beq $19, $0, cont_reset
		beq $0, $0 no_reset
		
		cont_reset:
		addi $15, $0, 0		#resets consecutive counter if bit is zero
		
		no_reset:
		addi $17, $17, 1
		
	bne $17, $18, loop_bit
		
	beq $0, $0, after_one
	
	oneoneone:
	addi $23, $23, 1	#oneone
		
	after_one:
	addi $9, $9, -1		#after_one
	addi $10, $10, 1
	addi $17, $0, 0
	addi $15, $0, 0
	
bne $9, $0, loop_bii
	
ori $14, $0, 0x2008
sb $23, 0($14)


# program end
