#=================================================================================
#
# Programmer : Jose A. Megret    CCOM 4017 Section 0U1
#                                First Semester 2024-2025
# Assignment 03                  Prof. Jose Ortiz Ubarri
# File : optimal.py              Date: November 7 2024
#
#=================================================================================

import sys

def optimal_page_replacement(num_pages, access_sequence):
    memory = []  # List to store pages currently in physical memory
    page_faults = 0  # Counter for page faults

    # Iterate over each access in the sequence
    for i, access in enumerate(access_sequence):
        page = access[2:]  # Extract the page number from access (e.g., 'R:5' -> '5')
        
        # If page is not in memory, a page fault occurs
        if page not in memory:
            page_faults += 1  # Increment page fault counter
            # If memory is not full, add the page directly
            if len(memory) < num_pages:
                memory.append(page)
            else:
                # Determine the page in memory that will not be used for the longest time
                future_uses = {
                    p: access_sequence[i+1:].index(f"R:{p}") if f"R:{p}" in access_sequence[i+1:] else float('inf')
                    for p in memory
                }
                # Find the page with the farthest or no future use
                page_to_replace = max(future_uses, key=future_uses.get)
                # Replace it with the new page
                memory[memory.index(page_to_replace)] = page
    
    print(f"Total page faults (Optimal): {page_faults}")

if __name__ == "__main__":
    # Ensure correct number of arguments (number of pages and file path)
    if len(sys.argv) != 3:
        print("Usage: python optimal.py <Number of physical memory pages> <access sequence file>")
        sys.exit(1)
    
    # Parse command-line arguments
    num_pages = int(sys.argv[1])  # Number of physical memory pages
    file_path = sys.argv[2]  # File containing memory access sequence

    # Read access sequence from the specified file
    with open(file_path, 'r') as f:
        access_sequence = f.read().split()

    # Run the Optimal page replacement simulation
    optimal_page_replacement(num_pages, access_sequence)
