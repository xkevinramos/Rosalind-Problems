import sys

def gc_content(file):
    # stores a read's gc percentage
    seq_dict = {}

    # Opens FASTA file for reading
    with open(file, 'r') as f:
        curr_seq = '' # keeps track of current read
        gc_counter = 0 # keeps track of GC count for a read
        at_counter = 0 # keeps tracks of AT count for a read

        for line in f:

            # new sequence
            if line[0] == '>':
                # Calculate GC percentage before analyzing new read
                if gc_counter > 0:
                    total = gc_counter + at_counter
                    seq_dict[curr_seq] = float((gc_counter / total)  * 100)

                # Store new seq id and reset
                curr_seq = line.replace('\n', '')[1:len(line) - 1]
                gc_counter = 0
                at_counter = 0
                seq_len = 0
                continue;

            else:
                # Checks read for GC and AT count
                for base in line:
                    if base == 'C' or base == 'G':
                        gc_counter += 1

                    if base == 'A' or base == 'T':
                        at_counter += 1

            # Handles the last read in the file
            seq_dict[curr_seq] = float((gc_counter / (at_counter + gc_counter))  * 100)

    # Access the read with the highest GC-content
    highest_gc = max(seq_dict.values())
    seq_id = ''
    for key, value in seq_dict.items():
        if highest_gc == value:
            seq_id = key

    # Formatting
    out = ' '.join(['Highest GC-content:', seq_id, str(value)])
    print(out)

    return seq_dict

# Allows user to pass in FASTA file in command line
gc_content(sys.argv[1])
