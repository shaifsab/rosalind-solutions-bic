def find_all_occurrences(pattern, genome):
    indices = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i+len(pattern)] == pattern:
            indices.append(i)
    indices_str = ''
    for index in indices:
        indices_str += str(index) + ' '
    return indices_str


print(find_all_occurrences('CTCGTAACT','CTCGTAACCTCGTAA'))