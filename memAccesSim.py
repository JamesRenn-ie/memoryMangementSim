import random

#class to simulate a program
class Program:
    def __init__(self, length, range=4):
        self.length = length
        self.range = range

    #generate a sequence of alphabet characters to simulate a programs memory requests
    def generateProgram(self):
        assert self.range in range(26), "Error: program Range must be < 25" #stops it going over alphabet limt
        programOptions = list(map(chr, range(97, 123)))
        access = []
        for _ in range(self.length):
            access.append(programOptions[random.randint(0,self.range)])
        self.code = access
    
            

#class to simulate memory
class Memory:
    mem = [] # the actual memory
    size = 3 # the size of memory
    controlOptions = ["default","fifo"] #all implemented control options, when adding new ones add them here
    def __init__(self, size, controlMethod):
        self.size = size
        self.controlMethod = controlMethod

    #simulate reading an item from memory, returns true if in memory or false if page fault
    #then adds the items to memory if it was a page fault
    def getItemFromMemory(self, item):
        print(self.mem)
        if item in self.mem:
            return True
        else:
            self.__addItemToMemory(item,"default")
            return False
        
    #adding items to memory with the passed control method
    def __addItemToMemory(self,item, method):
        assert method in self.controlOptions, "Control option not implemented, please use an implemented one." #checks it's only asking for an implemented method
        
        #just replaced the largest index in memory
        if method == "default":
            if len(self.mem) < self.size: #if the memory isn't full, append. If it is, change the last item.
                self.mem.append(item)
            else:
                self.mem[-1]=item

        #simulate first in first out
        if method == "fifo":
            tracker = []
            if len(self.mem) < self.size: #if the memory isn't full, append.
                self.mem.append(item)
                tracker.append(item)
            else:
                toRemove = tracker.pop
                indexToReplace = self.mem.index(toRemove)
                self.mem[indexToReplace]=item


class computer:
    def __init__(self, memSize=3, programLength=10, programRange=4, memControlMethod="default"):
        self.memory = Memory(memSize,memControlMethod)
        self.program = Program(programLength,programRange)

    def run(self):
        self.program.generateProgram()
        faults = 0
        for i in self.program.code:
            if self.memory.getItemFromMemory(i) == False:
                faults += 1
        print(f"Program ran succesfully with {faults} faults!")
        print(f"You used the '{self.memory.controlMethod}' method to control your memory")

def main():
    myPC = computer(programLength=1000, programRange=25, memControlMethod="fifo")
    myPC
    myPC.run()


if __name__ == "__main__":main()




    

