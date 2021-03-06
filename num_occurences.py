def num_occurences(dna_string):  
    # stores base counts
    occur_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # iterates through the string 
    for char in dna_string:
        occur_dict[char] += 1

    return occur_dict

sample = 'CACCATACGCTTTGGTTACCGAAATGGTCTGTCGCTACTGCCACGAGGACGCTCACGTCTATTTCGCTAGAAAAGCAACATTTCAAGAAGTTTCCGGCAAGGCCTAACAAGTAACCTCCCATTTTTTTTTGGCGGAATTGCCGGCCCGGCGTGCCCGCCTCAACAGTGATACCGATCCGTTACTAGTTCCCGGGGCCAAAACTGGCACGTCTCGAGCTAAGTCCTGGATTCAGGCTACGAATGTAAAGACATATGAATCGGACGAGCTCTGTGGTCTAGTAATGTTTAATACGGACCCGCACTCGCCGAGACTTGACAGCTGTTTTGATTATGGTTCGTCCATGGCGCGCACTCAGTGCACCACCCGCTAAAGTCTCGGACTCCCCGATAACGAGAATCTAACGAGATATGTCTGGTATCCACAATCGCACTATAACAATTGCGGCCCTCCTCGTCAGCCCTAGCTCGAATATATAAATGGGACGCCGAGCCGTGATAATCCGACGTACTAAACACTAACTAGTAGCAGGCCCTGTATGCTCCTTATTAAACGACACCACAGTCACCCTTTAACCGGCGGCTACCTTACCCTGGCGTTCGTTGTGATCTGAAATCATGTTTACTTGCCTATGGGCACATTGGAACGTATAACGCATTCATTAGGGCCGATATCAGTTCAACCGCGGCACGTGTTAGGAGTTAGCCAGGCCGCCATTCACCGGATATGCCTCCTACACACAGGGACAGGACTACCAACACGAAGTAAACTATGTGACAGTCCCGACTCGGAGGCGCCGGTACTAGACTTATCGTAATGAACATGCGCTCTTGATGGGGCAATCTATGTTTGAAGGTCGTTAAACCAATCTTAAATATAAGGGCCTCCTGGAGTACTGGAAATCGGTCAATGGATCGTGCCTACGCTGCGTGCGTATCACGCATT'
output_dict = num_occurences(sample)

print(output_dict['A'], output_dict['C'], output_dict['G'], output_dict['T'])
