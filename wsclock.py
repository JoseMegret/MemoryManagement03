#=================================================================================
#
# Programmer : Jose A. Megret    CCOM 4017 Section 0U1
#                                First Semester 2024-2025
# Assignment 03                  Prof. Jose Ortiz Ubarri
# File : wsclock.py              Date: November 7 2024
#
#=================================================================================

import sys
from collections import deque

def wsclock_page_replacement(num_pages, tau, access_sequence):
    memory = []  # List to store pages in physical memory
    last_used = {}  # Dictionary to track the last access time of each page
    page_faults = 0  # Counter for page faults
    clock = 0  # Logical clock to represent time

    # Iterate over each access in the sequence
    for access in access_sequence:
        page = access[2:]  # Extract the page number (e.g., 'R:5' -> '5')
        
        # If page is not in memory, a page fault occurs
        if page not in memory:
            page_faults += 1  # Increment page fault counter
            
            # If memory has space, simply add the page
            if len(memory) < num_pages:
                memory.append(page)
            else:
                # Loop to find a suitable page to replace
                while True:
                    page_to_replace = memory[0]  # Check the page at the "clock hand" position
                    
                    # If the page hasn't been used within the last tau ticks, replace it
                    if clock - last_used.get(page_to_replace, 0) > tau:
                        memory.pop(0)  # Remove the page from memory
                        memory.append(page)  # Add the new page
                        break
                    else:
                        # Move the clock hand forward by rotating the memory queue
                        memory.append(memory.pop(0))
        
        # Update last access time for the current page
        last_used[page] = clock
        clock += 1  # Advance the logical clock for each page access
    
    print(f"Total page faults (WSClock): {page_faults}")

if __name__ == "__main__":
    # Ensure the correct number of arguments (number of pages, tau, and file path)
    if len(sys.argv) != 4:
        print("Usage: python wsclock.py <Number of physical memory pages> <tau> <access sequence file>")
        sys.exit(1)
    
    # Parse command-line arguments
    num_pages = int(sys.argv[1])  # Number of physical memory pages
    tau = int(sys.argv[2])  # Time interval for page replacement decisions
    file_path = sys.argv[3]  # File containing memory access sequence

    # Read access sequence from the specified file
    with open(file_path, 'r') as f:
        access_sequence = f.read().split()

    # Run the WSClock page replacement simulation
    wsclock_page_replacement(num_pages, tau, access_sequence)
