
lui $8, 64025
ori $8, $8, 58214


addi $9, $0, 1

addi $10, $0, 100

addi $11, $0, 8224
addi $12,$0,0
addi $13, $0, 0
addi $14,$0,0
addi $15,$0,5

loop:

add $12,$0,$9

mult_xor:
multu $12, $8
mfhi $13
mflo $14
xor $12, $13,$14
addi $15,$15,-1
bne $15,$0,mult_xor
addi $15,$0,5


sll $13, $12, 16
srl $13, $13, 16
srl $14, $12, 16

xor $12, $14, $13

sll $13, $12, 24
srl $13, $13, 24
srl $14, $12, 8

xor $12, $12, $23
sw $0, 0($11)


sw $12, 0($11)
addi $9, $9, 1
addi $10, $10, -1
addi $11, $11, 4
bne $10, $0, loop
addi $20, $0, 0



addi $9, $0, 0
addi $10, $0, 99
addi $11, $0, 8224
addi $12, $0, 0
addi $13, $0, 0
lw $8, 0($11)
addi $11, $11, 4

loop_max:
lw $9, 0($11)
sltu $12, $9, $8

		 
bne $12, $0, skip

add $8, $0, $9
add $13, $0, $11
skip:

addi $11, $11, 4
addi $10, $10, -1
bne $10, $0, loop_max

addi $11, $0, 8192
sw $13, 0($11)
sw $8, 4($11)


addi $11, $0, 8224
addi $8,$0,0
addi $9, $0, 0
addi $12, $0, 100

addi $13,$0,0
addi $14,$0,4
pattern_loop:
lw $8, 0($11)
addi $10,$0,0
consecutive_ones:
andi $13,$8,1
addi $22, $0, 1
bne $13,$22, not_one
addi $10,$10,1

not_one:
bne $13,$0, is_one

addi $10,$0,0
is_one:

sltu $13, $14,$10
bne $13,$22, no_5_consecutive_ones
addi $9,$9,1
no_5_consecutive_ones:
bne $13, $0, yes_consecutive_ones

srl $8,$8,1
bne $8,$0, consecutive_ones


yes_consecutive_ones:
addi $12,$12,-1
addi $11,$11,4
bne $12,$0, pattern_loop

addi $13, $0, 8200
sw $9, 0($13)

