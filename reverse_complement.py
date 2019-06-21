import sys
def reverse_complement(seq):
    # dictionary to access a base's complement
    comp_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    # stores reverse complement string
    rev = ''

    # iterate through each base
    for base in seq:
        # access base in dictionary and append complement
        rev = comp_dict[base] + rev

    return rev

print(reverse_complement(sys.argv[1]))

