# $8 = B
lui $8, 0xFA19
ori $8, $8, 0xE366 

# $9 = A
addi $9, $0, 1

addi $10, $0, 100 #counter

addi $11, $0, 0x2020 #starting address
addi $12,$0,0 # $12 = C, and the results of folding
addi $13, $0, 0 #To store hi, to store upper half of word
addi $14,$0,0 #To store lo, to store lower half of word
addi $15,$0,5 #amount of times to mult and fold

loop:
#Multiplying and Folding proccess
add $12,$0,$9 # C = An

mult_xor:
multu $12, $8
mfhi $13
mflo $14
xor $12, $13,$14
addi $15,$15,-1
bne $15,$0,mult_xor
addi $15,$0,5 #setting counter back to 5
#folding 2 more times
#first fold, storing C into memory so I can access half of the word
sw $12, 0($11)
lhu $13, 0($11)
lhu $14, 2($11)
xor $12, $14, $13
#second fold
sw $12, 0($11)
srl $23, $12, 8
andi $12,$12,0xFF

xor $12, $12, $23
sw $0, 0($11) #resetting the address $11 to 0's 

#storing result C into address and moving on
sw $12, 0($11) #storing content of $9 to address in $11
addi $9, $9, 1 #moving on to next digit
addi $10, $10, -1 #decreasing counter by one
addi $11, $11, 4 #moving on to next word
bne $10, $0, loop
addi $20, $0, 0

#finding the max C value. Storing the value in 0x2004 and the address in 0x2000

addi $9, $0, 0 #the current value
addi $10, $0, 99 #counter
addi $11, $0, 0x2020 #starting address
addi $12, $0, 0 #will store the result of sltu (1 or 0)
addi $13, $0, 0 #the current max value's address
lw $8, 0($11) #the current max Value, at the beginning, the max value is the first one
addi $11, $11, 4

loop_max:
lw $9, 0($11) #loading the value in the current address into register
sltu $12, $9, $8 #Checking if the current value is less than the current max.
		 #If yes, then $12 is 1, otherwise its 0
		 
bne $12, $0, skip

add $8, $0, $9 #copying the new max value into the current max value
add $13, $0, $11#copying the new max value's address
skip:

addi $11, $11, 4
addi $10, $10, -1
bne $10, $0, loop_max

addi $11, $0, 0x2000
sw $13, 0($11)
sw $8, 4($11)

#pattern matching
addi $11, $0, 0x2020 #starting address
addi $8,$0,0 # hold the current value in the current address
addi $9, $0, 0 #Counter for number of Y's
addi $12, $0, 100 #counter

addi $13,$0,0 #temp register
addi $14,$0,4#used to compare later
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

