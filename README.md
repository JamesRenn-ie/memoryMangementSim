# memoryMangementSim
A simulator for basic memory mangement methods, to see which one is most efficient. Coded in object orientated python.


running the file by deafult will run with parameters:
self, memSize=3, programLength=1000, programRange=4, memControlMethod="fifo"

memSize is how many pages are in memory, program length is how long the list of characters is, program range is the range of differente characters that can exist (eg a-z is 25) mem control method is the method you use to control memory

This will simulate a 'program' which is a series of random characters form the alphabet, and fetching them from memory. If they don't appear in memory this is a page fault, and they will be added to memory using the specified scheme. It will tell you afterwards how many page faults there were for the scheme.

## Currently implemented schemes:
Deafult - just replaces the last item index in memory with the new item.\
FIFO - first in first out, replaces the thing that went into memory first with the new item.

## Drawbacks
The systems 'program' is entirely random, so doesn't allow for the fact that usually things that are accesses recently are more popular. This will mean it doesn't accurately affect real world usage, but is more of a worst case test.
