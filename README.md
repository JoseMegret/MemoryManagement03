# Memory Management Project - Page Replacement Algorithms
## Overview

This project simulates three page replacement algorithms commonly used in operating systems for memory management:

    FIFO (First-In-First-Out) Page Replacement
    Optimal Page Replacement
    WSClock Page Replacement

Each algorithm simulates the management of physical memory by keeping a fixed number of pages in memory (num_pages) and replacing pages based on specific rules when memory is full. The goal is to observe the number of page faults that occur as a sequence of memory requests is processed.
## Algorithms
### 1. FIFO (First-In-First-Out) Page Replacement

The FIFO page replacement algorithm replaces the oldest page in memory whenever a new page is loaded, and memory is full. This algorithm uses a queue structure to keep track of pages in memory, ensuring that the oldest page (the first one in the queue) is removed when necessary.

    Implementation: FIFO uses a deque with a maximum size of num_pages.
    Command: python fifo.py <Number of physical memory pages> <access sequence file>

### 2. Optimal Page Replacement

The Optimal Page Replacement algorithm minimizes page faults by replacing the page that will not be used for the longest time in the future. This requires analyzing the future access sequence to determine which page to replace.

    Implementation: The optimal algorithm calculates the next use of each page in memory and replaces the page with the farthest future use.
    Command: python optimal.py <Number of physical memory pages> <access sequence file>

### 3. WSClock Page Replacement

The WSClock page replacement algorithm uses a circular approach and a reference bit to decide which page to replace. Pages are given a "second chance" to remain in memory if accessed within a specified time window (tau). If a page’s reference bit is 0 and it hasn't been used within tau ticks, it becomes a candidate for replacement.

    Implementation: The algorithm simulates a clock hand moving through memory to evaluate each page for replacement.
    Command: python wsclock.py <Number of physical memory pages> <tau> <access sequence file>

## Usage
### Requirements

* Python 3.x

## Running Each Algorithm

To run each algorithm, use the command-line syntax below, specifying:

* num_pages: Number of physical memory pages.
* access_sequence_file: File containing the sequence of memory access requests.

#### FIFO Algorithm:

    python fifo.py <Number of physical memory pages> <access sequence file>

#### Optimal Algorithm:

    python optimal.py <Number of physical memory pages> <access sequence file>

#### WSClock Algorithm:

    python wsclock.py <Number of physical memory pages> <tau> <access sequence file>

### Example Usage

For example, to run each algorithm with 10 pages and test1.txt as the input file, use:

    python fifo.py 10 test1.txt
    python optimal.py 10 test1.txt
    python wsclock.py 10 5 test1.txt

### Input File Format

The input file (access_sequence_file) should contain a sequence of memory access requests in the format R:<page_number> for reads or W:<page_number> for writes, separated by spaces or new lines. For instance:

    R:1 W:2 R:3 W:4 R:5

## Example Output

Each algorithm outputs the total number of page faults that occurred during the simulation. For example:

    Total page faults (FIFO): 24

## Explanation of Each Algorithm
### FIFO (First-In-First-Out) Algorithm

    Description: The FIFO algorithm maintains a queue of pages in memory. When a page needs to be replaced, the oldest page (i.e., the page that has been in memory the longest) is removed.
    Usage: Simple to implement and uses minimal data structures.

### Optimal Page Replacement Algorithm

    Description: The Optimal algorithm keeps track of future page requests and replaces the page that will not be used for the longest time. This algorithm is often used as a benchmark because it provides the minimum possible page faults but requires knowledge of future accesses.
    Usage: Ideal for studying theoretical performance but not feasible in real systems due to the need for future knowledge.

### WSClock Page Replacement Algorithm

    Description: The WSClock algorithm works by moving a "clock hand" through pages in memory. Pages accessed recently have their reference bits set, and those not used within the last tau time ticks are replaced. This is a practical version of the Clock algorithm with added support for working sets.
    Usage: Useful in systems where memory pages have varying access patterns, and pages used frequently remain in memory longer.

## File Descriptions

Each .py file in this project corresponds to a specific page replacement algorithm. Detailed comments are provided in each file to explain key parts of the code. The main files include:

    fifo.py: Implementation of FIFO page replacement.
    optimal.py: Implementation of Optimal page replacement.
    wsclock.py: Implementation of WSClock page replacement.

## Acknowledgments

    University of Puerto Rico: This project is part of the CCOM4017 Operating Systems course.
    Professor's Guidance: The assignment instructions and example input files were provided by the course instructor.
