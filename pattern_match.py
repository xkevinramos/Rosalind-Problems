import sys
def pattern_match(file):
    # stores match positions
    positions = []
    # open file for reading
    with open(file, 'r') as f:
        # store the first line containing the pattern
        pattern = f.readline().rstrip()
        # store the second line containing text
        text = f.readline().rstrip()

        # shifts frame until it can no longer fit the pattern
        for i in range(len(text) - len(pattern) + 1):
            # checks if current frame matches the pattern
            if text[i:i + len(pattern)] == pattern:
                # stores index for matches
                positions.append(i)

    return positions

pos = pattern_match(sys.argv[1])
print(*pos)
