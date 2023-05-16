def approximate_pattern_matching():
    pattern = input("Enter the pattern: ")
    text = input("Enter the text: ")
    d = int(input("Enter the maximum number of mismatches: "))
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if sum([1 for j in range(len(pattern)) if pattern[j] != text[i+j]]) <= d:
            positions.append(i)
    return positions


print(approximate_pattern_matching())