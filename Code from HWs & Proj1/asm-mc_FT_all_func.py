# Author: Trung Le


# Remember where each of the jump label is, and the target location 
def saveJumpLabel(asm,labelIndex, labelName):
    lineCount = 0
    for line in asm:
        line = line.replace(" ","")
        if(line.count(":")):
            labelName.append(line[0:line.index(":")]) # append the label name
            labelIndex.append(lineCount) # append the label's index
            asm[lineCount] = line[line.index(":")+1:]
        lineCount += 1
    for item in range(asm.count('\n')): # Remove all empty lines '\n'
        asm.remove('\n')

def main():
    labelIndex = []
    labelName = []
    f = open("mc.txt","w+")
    h = open("mips.asm","r")
    asm = h.readlines()
    for item in range(asm.count('\n')): # Remove all empty lines '\n'
        asm.remove('\n')

    saveJumpLabel(asm,labelIndex,labelName) # Save all jump's destinations
    
    for line in asm:
        line = line.replace("\n","") # Removes extra chars
        line = line.replace("$","")
        line = line.replace(" ","")
        line = line.replace("zero","0") # assembly can also use both $zero and $0

        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # ~ ~ ~ ~ ~ ~ ~ ~ GIVEN

        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # ~ ~ ~ ~ ~ ~ ~ MY WORK

        # = = = = ADDIU = = = = = = = = (I)
        if(line[0:5] == "addiu"):
            line = line.replace("addiu", "")    # delete the addiu from the string.
            line = line.split(",")              # split the 1 string 'line' into a string array of many strings, broken at the comma.
            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            rs = format(int(line[1]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            imm = format(int(line[2]),'016b') if (int(line[2]) > 0) else format(65536 + int(line[2]),'016b')
            f.write(str('001001') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = ADDI = = = = = = (I)
        elif(line[0:4] == "addi"):
            line = line.replace("addi","")
            line = line.split(",")
            imm = format(int(line[2]),'016b') if (int(line[2]) > 0) else format(65536 + int(line[2]),'016b')
            rs = format(int(line[1]),'05b')
            rt = format(int(line[0]),'05b')
            f.write(str('001000') + str(rs) + str(rt) + str(imm) + '\n')


        # = = = = ADD = = = = = = (R)
        elif(line[0:3] == "add"):
            line = line.replace("add","")
            line = line.split(",")
            rd = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rs = format(int(line[1]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rt = format(int(line[2]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000100000') + '\n')
                # the last part is actually accounting for sh = 00000 (5 zeroes)
                # and 6 bits for the func (0x20) = 100000

        # = = = = MULTU = = = = = = = = (R)
        elif(line[0:5] == "multu"):
            line = line.replace("multu","")
            line = line.split(",")

            rs = format(int(line[0]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            rt = format(int(line[1]),'05b') # make element 2 in the set, 'line' an int of 5 bits. (rt)

            
            f.write(str('000000') + str(rs) + str(rt) + str('00000') + str('00000') + str('011001') + '\n')
            

        # = = = = MULT = = = = = = = = (R)
        elif(line[0:4] == "mult"):
            line = line.replace("mult","")
            line = line.split(",")
            rs = format(int(line[0]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            rt = format(int(line[1]),'05b') # make element 2 in the set, 'line' an int of 5 bits. (rt)
            f.write(str('000000') + str(rs) + str(rt) + str('00000') + str('00000') + str('011000') + '\n')


        # = = = = SRL = = = = = = = = (R)
        elif(line[0:3] == "srl"):
            line = line.replace("srl","")
            line = line.split(",")
            rd = format(int(line[0]),'05b')  # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rt = format(int(line[1]),'05b')  # make element 2 in the set, 'line' an int of 5 bits. (rt)
            sh = format(int(line[2]), '05b') # make element 3 in the set, 'line' an int of 5 bits. (sh)
            f.write(str('000000') + str('00000') + str(rt) + str(rd) + str(sh) + str('000010') + '\n')


        # = = = = LB = = = = = = = = = (I)
        elif(line[0:2] == "lb"):
            line = line.replace(")", "")    # remove the ) paran entirely.
            line = line.replace ("(", ",")  # replace ( left paren with comma

            line = line.replace("lb", "")    
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.
            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('100000') + str(rs) + str(rt) + str(imm) + '\n')


        # = = = = SB = = = = = = = = = (I)
        elif(line[0:2] == "sb"):
            line = line.replace(")", "")    # remove the ) paran entirely.
            line = line.replace ("(", ",")  # replace ( left paren with comma

            line = line.replace("sb", "")    
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.


            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('101000') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = LW = = = = = = = = = (I)
        elif(line[0:2] == "lw"):
            line = line.replace(")", "")    # remove the ) paran entirely.
            line = line.replace ("(", ",")  # replace ( left paren with comma

            line = line.replace("lw", "")    
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.
            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('100011') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = SW = = = = = = = = = (I)
        elif(line[0:2] == "sw"):
            line = line.replace(")", "")    # remove the ) paran entirely.
            line = line.replace ("(", ",")  # replace ( left paren with comma

            line = line.replace("sw", "")   
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.
            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('101011') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = LUI = = = = = = = = = (I)
        elif(line[0:3] == "lui"):
            line = line.replace("lui", "")   
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.

            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            f.write(str('001111') + str('00000') + str(rt) + str(imm) + '\n')

        # = = = = ORI = = = = = = = = = (I)
        elif(line[0:3] == "ori"):
            line = line.replace("ori", "")   
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.

            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('001101') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = ANDI = = = = = = = = = (I)
        elif(line[0:4] == "andi"):
            line = line.replace("andi", "")   
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.

            rt = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rt)
            imm = format(int(line[1]),'016b') if (int(line[1]) >= 0) else format(65536 + int(line[1]),'016b')
            rs = format(int(line[2]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            f.write(str('001100') + str(rs) + str(rt) + str(imm) + '\n')

        # = = = = AND = = = = = = = = = (R)
        elif(line[0:4] == "andi"):
            line = line.replace("andi", "")   
            line = line.split(",")           # split the 1 string 'line' into a string array of many strings, broken at the comma.

            rd = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rs = format(int(line[1]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rt = format(int(line[2]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000') + str('100100') + '\n')

        # = = = = MFHI = = = = = = = = (R)
        elif(line[0:4] == "mfhi"):
            line = line.replace("mfhi","")
            line = line.split(",")
            rd = format(int(line[0]),'05b')  # make element 0 in the set, 'line' an int of 5 bits. (rd)
            f.write(str('000000') + str('00000')+ str('00000') + str(rd) + str('00000') + str('010000') + '\n')

        # = = = = MFLO = = = = = = = = (R)
        elif(line[0:4] == "mflo"):
            line = line.replace("mflo","")
            line = line.split(",")
            rd = format(int(line[0]),'05b')  # make element 0 in the set, 'line' an int of 5 bits. (rd)
            f.write(str('000000') + str('00000')+ str('00000') + str(rd) + str('00000') + str('010010') + '\n')

        # = = = = XOR = = = = = = = = (R)
        elif(line[0:3] == "xor"):
            line = line.replace("xor","")
            line = line.split(",")
            rd = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rs = format(int(line[1]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rt = format(int(line[2]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            f.write(str('000000') + str(rs)+ str(rt) + str(rd) + str('00000') + str('100110') + '\n')

        # = = = = BEQ = = = = = = = = = (I)
        elif(line[0:3] == "beq"):
            line = line.replace("beq","")
            line = line.split(",")
            #print(line)
            rt = format(int(line[0]),'05b')
            rs = format(int(line[1]),'05b')
                #imm = format(int(line[2]),'016b') if (int(line[2]) > 0) else format(65536 + int(line[2]),'016b')
            for i in range(len(labelName)):
                if(labelName[i] == line[0]):
                    f.write(str('000101') + str(rs) + str(rt) + str(format(int(labelIndex[i]),'016b')) + '\n')

        # = = = = BNE = = = = = = = = = (I)
        elif(line[0:3] == "bne"):
            line = line.replace("bne","")
            line = line.split(",")
            #print(line)
            rt = format(int(line[0]),'05b')
            rs = format(int(line[1]),'05b')
                #imm = format(int(line[2]),'016b') if (int(line[2]) > 0) else format(65536 + int(line[2]),'016b')
            for i in range(len(labelName)):
                if(labelName[i] == line[0]):
                    f.write(str('000101') + str(rs) + str(rt) + str(format(int(labelIndex[i]),'016b')) + '\n')

        # = = = = SLTU = = = = = = = = = (R)
        elif(line[0:4] == "sltu"):
            line = line.replace("sltu","")
            line = line.split(",")
            rd = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rs = format(int(line[1]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            rt = format(int(line[2]),'05b') # make element 2 in the set, 'line' an int of 5 bits. (rt)

            for i in range(len(labelName)):
                if(labelName[i] == line[0]):
                    f.write(str('000101') + str(rs) + str(rt) + str(format(int(labelIndex[i]),'016b')) + '\n')

        # = = = = SLT = = = = = = = = = (R)
        elif(line[0:3] == "slt"):
            line = line.replace("slt","")
            line = line.split(",")
            rd = format(int(line[0]),'05b') # make element 0 in the set, 'line' an int of 5 bits. (rd)
            rs = format(int(line[1]),'05b') # make element 1 in the set, 'line' an int of 5 bits. (rs)
            rt = format(int(line[2]),'05b') # make element 2 in the set, 'line' an int of 5 bits. (rt)
            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000') + str('101010') + '\n')

        # = = = = JUMP = = = = = = (J)
            
        elif(line[0:1] == "j"): 
            line = line.replace("j","")
            line = line.split(",")

            # Since jump instruction has 2 options:
            # 1) jump to a label
            # 2) jump to a target (integer)
            # We need to save the label destination and its target location

            if(line[0].isdigit()): # First,test to see if it's a label or a integer
                f.write(str('000010') + str(format(int(line[0]),'026b')) + '\n')

            else: # Jumping to label
                for i in range(len(labelName)):
                    if(labelName[i] == line[0]):
                        f.write(str('000010') + str(format(int(labelIndex[i]),'026b')) + '\n')



    f.close()

if __name__ == "__main__":
    main()