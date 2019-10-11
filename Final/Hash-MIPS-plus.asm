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
xor $12, $13, $14
sw $0, 0($11)
sw $12, 0($11)
comp $19, $12, 0
add $21, $21, $19
addi $9, $9, 1
addi $10, $10, -1
addi $11, $11, 4
bne $10, $0, loop
addi $20, $0, 0
addi $15, $15, 0
addi $14, $14, 0
addi $18, $18, 0
loop_pattern:
addi $22, $0, 8200
sw $21, 0($22)