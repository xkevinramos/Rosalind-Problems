def num_occurences(dna_string):
    """
    Calculate the number of occurences for the nucleotides in the given DNA
    strand.

    Parameters
    ----------
    dna_string : string
        The DNA strand we are evaluating.

    Returns
    -------
    occur_dict : dictionary
        A dictionary containing the result of counting all the nucleotides in
        the DNA strand.
    """

    occur_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for char in dna_string:
        occur_dict[char] += 1

    return occur_dict

sample = 'CACCATACGCTTTGGTTACCGAAATGGTCTGTCGCTACTGCCACGAGGACGCTCACGTCTATTTCGCTAGAAAAGCAACATTTCAAGAAGTTTCCGGCAAGGCCTAACAAGTAACCTCCCATTTTTTTTTGGCGGAATTGCCGGCCCGGCGTGCCCGCCTCAACAGTGATACCGATCCGTTACTAGTTCCCGGGGCCAAAACTGGCACGTCTCGAGCTAAGTCCTGGATTCAGGCTACGAATGTAAAGACATATGAATCGGACGAGCTCTGTGGTCTAGTAATGTTTAATACGGACCCGCACTCGCCGAGACTTGACAGCTGTTTTGATTATGGTTCGTCCATGGCGCGCACTCAGTGCACCACCCGCTAAAGTCTCGGACTCCCCGATAACGAGAATCTAACGAGATATGTCTGGTATCCACAATCGCACTATAACAATTGCGGCCCTCCTCGTCAGCCCTAGCTCGAATATATAAATGGGACGCCGAGCCGTGATAATCCGACGTACTAAACACTAACTAGTAGCAGGCCCTGTATGCTCCTTATTAAACGACACCACAGTCACCCTTTAACCGGCGGCTACCTTACCCTGGCGTTCGTTGTGATCTGAAATCATGTTTACTTGCCTATGGGCACATTGGAACGTATAACGCATTCATTAGGGCCGATATCAGTTCAACCGCGGCACGTGTTAGGAGTTAGCCAGGCCGCCATTCACCGGATATGCCTCCTACACACAGGGACAGGACTACCAACACGAAGTAAACTATGTGACAGTCCCGACTCGGAGGCGCCGGTACTAGACTTATCGTAATGAACATGCGCTCTTGATGGGGCAATCTATGTTTGAAGGTCGTTAAACCAATCTTAAATATAAGGGCCTCCTGGAGTACTGGAAATCGGTCAATGGATCGTGCCTACGCTGCGTGCGTATCACGCATT'
output_dict = num_occurences(sample)

print(output_dict['A'], output_dict['C'], output_dict['G'], output_dict['T'])