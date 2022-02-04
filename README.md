# synacor_challenge

This repository contains code that solves the Synacor Challenge. It contains the following programs:

`vm.py` - virtual machine in Python implementing the instruction set specified in the challenge. Also disassembles the input program for use in
reverse engineering the teleporter verification.

`modified_ackermann.py` - prototype to solve the teleporter verification problem using Python's built-in caching.

`ackermann.jl` - dynamic programming prototype to solve the teleporter verification problem in Julia.

`modified_ackermann.cpp` - final program to solve the teleporter verification code using dynamic programming and 16-bit integers to avoid stack overflow.

`bfs.py` - graph search to find the shortest path to unlock the vault for the final code in the challenge.
