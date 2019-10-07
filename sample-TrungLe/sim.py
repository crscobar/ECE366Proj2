# Author: Trung Le
# Supported instrs: 
# addi, sub, beq, ori, sw



def sim(program):
    finished = False      # Is the simulation finished? 
    PC = 0                # Program Counter
    register = [0] * 32   # Let's initialize 32 empty registers
    mem = [0] * 12288     # Let's initialize 0x3000 or 12288 spaces in memory. I know this is inefficient...
                          # But my machine has 16GB of RAM, its ok :)
    DIC = 0               # Dynamic Instr Count
    while(not(finished)):
        if PC == len(program) - 4: 
            finished = True
        fetch = program[PC]
        DIC += 1
        #print(hex(int(fetch,2)), PC)
        if fetch[0:6] == '001000': # ADDI
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            imm = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)
            register[t] = register[s] + imm
            
        elif fetch[0:6] == '000000' and fetch[21:32] == '00000100010': # SUB
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            d = int(fetch[16:21],2)
            register[d] = register[s] - register[t]
            
        elif fetch[0:6] == '000100':  # BEQ
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            imm = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)
            # Compare the registers and decide if jumping or not
            if register[s] == register[t]:
                PC += imm*4
        
        elif fetch[0:6] == '001101':   # ORI
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            imm = int(fetch[16:],2)
            register[t] = register[s] | imm

        elif fetch[0:6] == '101011':  # SW
            PC += 4
            s = int(fetch[6:11],2)
            t = int(fetch[11:16],2)
            offset = -(65536 - int(fetch[16:],2)) if fetch[16]=='1' else int(fetch[16:],2)
            offset = offset + register[s]
            mem[offset] = register[t]

        else:
            # This is not implemented on purpose
            print('Not implemented')

    # Finished simulations. Let's print out some stats
    print('***Simulation finished***')
    print('Registers $8 - $23 ', register[8:23])
    print('Dynamic Instr Count ', DIC)
    print('Memory contents 0x2000 - 0x2050 ', mem[8192:8272])




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
