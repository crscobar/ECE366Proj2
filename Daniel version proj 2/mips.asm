addi $3,$0,8192
addi $14,$0,4
addi $5,$12,-4
beq $5, $0, TEST
bne $5, $0, TEST2
sw $5, 1($3)
lw $9, 1($3)
sb $5, 4($3)
lb $10, 4($3)
addiu $11,$14,-4
add $2,$4,$zero
L1:add $1,$0,$8
add $7,$7,$8
TEST2:
addi $3,$3,-2
TEST: addi $2,$5,-1
mult $14,$14
multu $14,$14
srl $14, $14,1
slt $2,$14,$5
sltu $2,$14,$5
j L1