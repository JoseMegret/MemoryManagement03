#=================================================================================
#
# Programmer : Jose A. Megret    CCOM 4017 Section 0U1
# Stu.Num : 801-21-7986          First Semester 2024-2025
# Assignment 03                  Prof. Jose Ortiz Ubarri
# File : fifo.py                 Date: November 7 2024
#
#=================================================================================

import sys
from collections import deque

# Simulate FIFO page replacement
def fifo_page_replacement(num_pages, access_sequence):
    memory = deque(maxlen=num_pages)  # Queue to hold pages in physical memory
    page_faults = 0  # Counter for page faults

    for access in access_sequence:
        page = access[2:]  # Get page number from access request
        if page not in memory:  # Check if page is already in memory
            page_faults += 1  # Increment page fault counter if not in memory
            memory.append(page)  # Add new page, removing oldest if memory is full
    
    print(f"Total page faults (FIFO): {page_faults}")

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fifo.py <Number of physical memory pages> <access sequence file>")
        sys.exit(1)
    
    num_pages = int(sys.argv[1])  # Number of pages in physical memory
    file_path = sys.argv[2]  # File containing memory access sequence

    # Read access sequence from the file
    with open(file_path, 'r') as f:
        access_sequence = f.read().split()

    # Run FIFO page replacement simulation
    fifo_page_replacement(num_pages, access_sequence)
