# Author: Trung Le
# Supported instrs: 
# addi, sub, beq, ori, sw



def sim(program):
    finished = False      # Is the simulation finished? 
    PC = 0                # Program Counter
    register = [0] * 32   # Let's initialize 32 empty registers
    mem = [0] * 12288     # Let's initialize 0x3000 or 12288 spaces in memory. I know this is inefficient...

    DIC = 0               # Dynamic Instr Count
    while(not(finished)):
        if PC == len(program) - 4: 
            finished = True
            register[3] = PC + 4

        fetch = program[PC]

        DIC += 1
        #print(hex(int(fetch,2)), PC)

#-------Chris' Sim Instructions-------------------------------------------------------------------------------------#
        # LUI
        if fetch[0:6] == '001111':  # LUI (I) || WORKING
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            imm = int(fetch[16:],2)
            
            register[rt] = imm << 16

        # ORI
        elif fetch[0:6] == '001101':   # ORI (I) || GIVEN
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            imm = int(fetch[16:],2)

            register[rt] = register[rs] | imm

        # ADDI
        elif fetch[0:6] == '001000': # ADDI (I) || GIVEN
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            imm = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)

            register[rt] = register[rs] + int(imm)

        # MULTU
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000011001':   # MULTU (R) || WORKING
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            rd = int(fetch[16:21],2)

            tempVar = register[rs] * register[rt]
            tempLo = format(tempVar, '064b')
            tempLo = tempVar & 0x00000000FFFFFFFF
            tempHi = tempVar >> 32

            register[1] = int(tempLo)
            register[2] = int(tempHi)

        # MFHI
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000010000':   # MFHI (R) || WORKING
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            rd = int(fetch[16:21],2)

            register[rd] = register[2]   # register 2 saved for hi

        # MFLO
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000010010':   # MFLO (R) || WORKING
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            rd = int(fetch[16:21],2)

            register[rd] = register[1]   # register 1 saved for lo

        # XOR
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000100110':   # XOR (R) || WORKING
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            rd = int(fetch[16:21],2)

            register[rd] = register[rs] ^ register[rt]     # ^ is XOR in python

        # SRL
        elif fetch[0:6] == '000000' and fetch[26:32] == '000010':  # SRL (R) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            rd = int(fetch[16:21], 2)
            sh = int(fetch[21:26], 2)

            register[rd] = int(register[rt]/(2**(sh)))

        # SLL
        elif fetch[0:6] == '000000' and fetch[26:32] == '000000':  # SLL (R) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            rd = int(fetch[16:21], 2)
            sh = int(fetch[21:26], 2)

            register[rd] = int(register[rt]*(2**(sh)))

        # SW
        elif fetch[0:6] == '101011':  # SW (I) || GIVEN
            PC += 4
            rs = int(fetch[6:11],2)
            rt = int(fetch[11:16],2)
            offset = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)
            offset = offset + register[rs]
            mem[offset] = register[rt]

        # LW
        elif fetch[0:6] == '100011':  # LW (I) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            imm = -(65536 - int(fetch[16:], 2)) if fetch[16] == '1' else int(fetch[16:], 2)
            imm = imm + register[rs]

            register[rt] = mem[imm]

        # ANDI
        elif fetch[0:6] == '001100':  # ANDI (I) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            imm = -(65536 - int(fetch[16:], 2)) if fetch[16] == '1' else int(fetch[16:], 2)

            register[rt] = register[rs] & imm

        # SLTU
        elif fetch[0:6] == '000000' and fetch[26:32] == '101011':  # SLTU (R) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            rd = int(fetch[16:21], 2)

            if register[rs] < register[rt]:
                register[rd] = 1
            else:
                register[rd] = 0

        # AND
        elif fetch[0:6] == '000000' and fetch[26:32] == '100100':  # AND (R) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            rd = int(fetch[16:21], 2)

            register[rd] = register[rs] & register[rt]

        # SB
        elif fetch[0:6] == '101000':  # SB (I) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            offset = -(65536 - int(fetch[16:], 2)) if fetch[16] == '1' else int(fetch[16:], 2)
            offset = offset + register[rs]
            mem[offset] = register[rt]

        # LB
        elif fetch[0:6] == '100000':  # LB (I) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            offset = -(65536 - int(fetch[16:], 2)) if fetch[16] == '1' else int(fetch[16:], 2)
            offset = offset + register[rs]
            register[rt] = mem[offset]

        # BEQ
        elif fetch[0:6] == '000100':  # BEQ (I) || GIVEN
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            imm = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)
            # Compare the registers and decide if jumping or not
            if register[s] == register[t]:
                PC += imm*4

        # BNE
        elif fetch[0:6] == '000101':  # BNE (I) || WORKING
            PC += 4
            rs = int(fetch[6:11], 2)
            rt = int(fetch[11:16], 2)
            imm = -(65536 - int(fetch[16:], 2)) if fetch[16] == '1' else int(fetch[16:], 2)
            # Compare the registers and decide if jumping or not
            if register[rs] != register[rt]:
                PC += imm * 4

        # SUB
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000100010': # SUB || GIVEN
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            d = int(fetch[16:21],2)
            register[d] = register[s] - register[t]

        else:
            # This is not implemented on purpose
            print('Not implemented')

    # Finished simulations. Let's print out some stats
    print('***Simulation finished***')
    print('Registers lo, hi, pc ', register[1:4])
    print('Registers $8 - $23 ', register[8:24])
    print('Dynamic Instr Count ', DIC)
    print('Memory contents 0x2000 - 0x2050 ', mem[8192:8272])

    input()


#----- MIPS File to MC Converter (HW4) ------#


def main():
    file = open('prog.asm')
    program = []
    for line in file:
        
        if line.count('#'):
            line = list(line)
            line[line.index('#'):-1] = ''
            line = ''.join(line)
        if line[0] == '\n':
            continue
        line = line.replace('\n','')
        instr = line[2:]
        instr = int(instr,16)
        instr = format(instr,'032b')
        program.append(instr)       # since PC increment by 4 every cycle,
        program.append(0)           # let's align the program code by every
        program.append(0)           # 4 lines
        program.append(0)

    # We SHALL start the simulation! 
    sim(program)     

if __name__ == '__main__':
    main()
