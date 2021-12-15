from collections import deque

class Machine:
    def __init__(self, fname) -> None:
        self.memory = [0 for _ in range(2**15)]
        self.registers = [0 for _ in range(8)]
        self.stack = deque()
        self.pc = 0
        self.console_buffer = ""
        with open(fname, "rb") as f:
            data = f.read()

        for i in range(0,len(data),2):
            self.memory[i//2] = data[i] + 256 * data[i+1]
            
    def get_arg(self, adr) -> int:
        arg = self.memory[adr]
        if arg >= 32768:
            return self.registers[arg-32768]
        return arg

    def get_arithmetic_args(self):
        reg = self.memory[self.pc+1] - 32768
        arg1 = self.get_arg(self.pc+2)
        arg2 = self.get_arg(self.pc+3)
        return reg, arg1, arg2
    
    def get_reg_arg(self):
        reg = self.memory[self.pc+1] - 32768
        arg = self.get_arg(self.pc+2)
        return reg, arg

    def exec_op(self) -> bool:
        opcode = self.memory[self.pc]
        nwords = 1
        if opcode == 0:
            return False
        elif opcode == 19:
            nwords = 2
            ch = chr(self.get_arg(self.pc+1))
            print(ch, end='')
        elif opcode == 21:
            pass
        elif opcode == 6:
            self.pc = self.memory[self.pc+1]
            return True
        elif opcode == 7:
            nwords = 3
            tval = self.get_arg(self.pc+1)
            j_adr = self.get_arg(self.pc+2)
            if tval:
                self.pc = j_adr
                return True
        elif opcode == 8:
            nwords = 3
            tval = self.get_arg(self.pc+1)
            j_adr = self.get_arg(self.pc+2)
            if not tval:
                self.pc = j_adr
                return True
        elif opcode == 1:
            nwords = 3
            reg, sv = self.get_reg_arg()
            self.registers[reg] = sv
        elif opcode == 9:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            res = (arg1 + arg2) % 32768
            self.registers[reg] = res
        elif opcode == 4:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = 1 * (arg1 == arg2)
        elif opcode == 2:
            nwords = 2
            v = self.get_arg(self.pc+1)
            self.stack.append(v)
        elif opcode == 3:
            if not self.stack:
                raise ValueError("attempted to pop empty stack")
            nwords = 2
            v = self.stack.pop()
            reg = self.memory[self.pc+1] - 32768
            self.registers[reg] = v
        elif opcode == 5:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = 1 * (arg1 > arg2)
        elif opcode == 12:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = arg1 & arg2
        elif opcode == 13:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = arg1 | arg2
        elif opcode == 14:
            nwords = 3
            reg, arg = self.get_reg_arg()
            self.registers[reg] = 32767 - arg
        elif opcode == 17:
            self.stack.append(self.pc+2)
            self.pc = self.get_arg(self.pc+1)
            return True
        elif opcode == 18:
            if not self.stack:
                return False
            ret_adr = self.stack.pop()
            self.pc = ret_adr
            return True
        elif opcode == 10:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = (arg1 * arg2) % 32768
        elif opcode == 11:
            nwords = 4
            reg, arg1, arg2 = self.get_arithmetic_args()
            self.registers[reg] = arg1 % arg2
        elif opcode == 15:
            nwords = 3
            reg, arg = self.get_reg_arg()
            self.registers[reg] = self.memory[arg]
        elif opcode == 16:
            nwords = 3
            v = self.get_arg(self.pc+2)
            mem_adr = self.get_arg(self.pc+1)
            self.memory[mem_adr] = v
        elif opcode == 20:
            nwords = 2
            if not self.console_buffer:
                self.console_buffer = input() + "\n"
            reg = self.memory[self.pc+1] - 32768
            self.registers[reg] = ord(self.console_buffer[0])
            self.console_buffer = self.console_buffer[1:]
        else:
            raise NotImplementedError()
        self.pc += nwords
        return True
    
    def exec(self) -> None:
        while self.exec_op() != False:
            pass

if __name__ == "__main__":
    m = Machine("challenge.bin")

    m.exec()

