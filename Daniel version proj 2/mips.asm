addi $10, $0, 255
addi $12, $0, 1
addi $13, $0, 8192
loop:
sb $12, 0($13)
addi $13, $13, 1
addi $10, $10, -1
addi $12, $12, 1
bne $10, $0, loop
addi $12, $12, -1
sb $12, 0($13)
addi $10, $0, 256
addi $13, $0, 8192
addi $14, $0, 0
addi $15, $0, 8
addi $16, $0, 0
addi $17, $0, 0
addi $18, $0, 0
addi $19, $0, 0
loop2:
lb $14, 0($13)
loop_and:
andi $18, $14, 1
beq $18, $0, skip
addi $17, $17, 1
skip:
srl $14, $14, 1
addi $15, $15, -1
bne $15, $0, loop_and


addi $15, $0, 8
sub $16, $15, $17

bne $16,$17, skip2

addi $19,$19,1
skip2:

addi $16, $0, 0
addi $17, $0, 0
addi $13, $13, 1
addi $10, $11, -1
bne $10, $0, loop2
