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

lui $8, 0xFA19
ori $8, $8, 0xE366


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

	sltu $17, $18, $8	#if new bit($18) < highest($8), then $17=1
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
#pattern matching

# $8 = curr val of curr addr
# $9 = Y counter
# $10 = consec 1 counter
# $11 = starting addr
# $12 = 100 loop counter
# $13 = temp register
# $14 = compare register
# $15 = 
# $16 = 
# $17 = 
# $18 = 
# $19 = 
# $20 = 
# $21 = 
# $22 = 5 consec 1 check
# $23 = 

addi $11, $0, 0x2020 #starting address
addi $8,$0,0 # hold the current value in the current address
addi $9, $0, 0 #Counter for number of Y's
addi $12, $0, 100 #counter

addi $13,$0,0 #temp register
addi $14,$0,4 #used to compare later

pattern_loop:
lw $8, 0($11) #loading the value in the current address into register
addi $10,$0,0 #Counter for number of consecutive 1's

consecutive_ones:
andi $13,$8,1 #if the rightmost bit is 1, then the result will be one
addi $22, $0, 1
bne $13,$22, not_one #if its a zero then we wont add to the 1's counter
addi $10,$10,1

not_one:
bne $13,$0, is_one #if it is one then we wont reset the 1's counter

addi $10,$0,0
is_one:

sltu $13, $14,$10
bne $13,$22, no_5_consecutive_ones #if there weren't 5 consecutive ones, then skip next line
addi $9,$9,1
no_5_consecutive_ones:
bne $13, $0, yes_consecutive_ones #if theres 5 consecutive ones already, then we dont need to check 
			          #the rest of the bits
srl $8,$8,1 #moving bits once to the right to check the next bit if it's one
bne $8,$0, consecutive_ones #when we shifted every single bit then the orignal number will be zero


yes_consecutive_ones:
addi $12,$12,-1
addi $11,$11,4
bne $12,$0, pattern_loop

addi $13, $0, 0x2008
sw $9, 0($13)


# program end
