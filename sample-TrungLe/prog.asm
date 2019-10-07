
# Test program
# 
0x20152020 # addi $21,$0,0x00002020
0x20122020 # addi $18,$0,0x00002020
0x2009ffff # addi $9,$0,-2
0x01031022 # sub $2,$8,$3
0x3508e366 # ori $8,$8,0x0000e366

0x12b20002 # beq $21,$18,0x00000002

0xad490000 # sw $9,0x00000000($10)
0xae52fffb # sw $18,-5($18)
# simulator can have comments in programs

# It can also have comment after the code
0xad490000 # sw $9,0x00000000($10)

