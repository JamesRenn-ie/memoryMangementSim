import random

#class to simulate a program
class Program:
    def __init__(self, length, range=4):
        self.length = length
        self.range = range

    #generate a sequence of alphabet characters to simulate a programs memory requests
    def generateProgram(self):

        # assert self.range in range(26), "Error: program Range must be < 25" #stops it going over alphabet limt
        # programOptions = list(map(chr, range(97, 123)))
        # access = []
        # for _ in range(self.length):
        #     access.append(programOptions[random.randint(0,self.range)])
        # self.code = access

        assert self.range in range(26), "Error: program Range must be < 25"
        programOptions = list(map(chr, range(97, 97 + self.range + 1)))

        # Create a weighted distribution where some letters appear more often
        frequent_pages = programOptions[: max(2, self.range // 2)]  # Most accessed half
        rare_pages = programOptions[max(2, self.range // 2) :]  # Less accessed half

        access = []
        for _ in range(self.length):
            if random.random() < 0.7:  # 70% chance to pick from frequent pages
                access.append(random.choice(frequent_pages))
            else:
                access.append(random.choice(rare_pages))

        self.code = access

    
            

#class to simulate memory
class Memory:
    controlOptions = ["default","fifo","lru"] #all implemented control options, when adding new ones add them here
    
    def __init__(self, size, controlMethod):
        self.size = size
        self.controlMethod = controlMethod
        self.tracker = [] #tracker used for differnt implementations
        self.mem = [] # the actual memory


    #simulate reading an item from memory, returns true if in memory or false if page fault
    #then adds the items to memory if it was a page fault
    def getItemFromMemory(self, item):
        if item in self.mem:
            return True
        else:
            self.__addItemToMemory(item,self.controlMethod)
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
            if len(self.mem) < self.size: #if the memory isn't full, append.
                self.mem.append(item)
                self.tracker.append(item)
            else:
                toRemove = self.tracker.pop(0)
                indexToReplace = self.mem.index(toRemove)
                self.mem[indexToReplace]=item
                self.tracker.append(item)
            
        
        if method == "lru":
            if item in self.mem:
                # If item is already in memory, move it to the most recently used position
                self.tracker.remove(item)
            else:
                if len(self.mem) >= self.size:
                    # Remove the least recently used item
                    lru_item = self.tracker.pop(0)
                    indexToReplace = self.mem.index(lru_item)  # Find where it is in memory
                    self.mem[indexToReplace] = item  # Replace it

                else:
                    self.mem.append(item)  # Just add if there's space

            # Update tracker to mark item as most recently used
            self.tracker.append(item)



class computer:
    def __init__(self, memSize=20, programLength=1000, programRange=25, memControlMethod="fifo"):
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
        return faults

def compare_algorithms(runs=1000, memSize=10, programLength=1000, programRange=25):
    fifo_faults = []
    lru_faults = []

    for _ in range(runs):
        fifo = computer(memSize=memSize, programLength=programLength, programRange=programRange, memControlMethod="fifo")
        lru = computer(memSize=memSize, programLength=programLength, programRange=programRange, memControlMethod="lru")

        fifo_faults.append(fifo.run())
        lru_faults.append(lru.run())

    avg_fifo = sum(fifo_faults) / runs
    avg_lru = sum(lru_faults) / runs

    print("\n--- Results ---")
    print(f"FIFO Average Page Faults: {avg_fifo:.2f}")
    print(f"LRU Average Page Faults: {avg_lru:.2f}")

def main():
    lru = computer(memControlMethod="lru")
    lru.run()

    fifo = computer(memControlMethod="fifo")
    fifo.run()
    # compare_algorithms()







if __name__ == "__main__":main()




    

