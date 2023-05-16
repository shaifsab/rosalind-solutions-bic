string = input("Enter a string: ")
k = int(input("Enter the length of the pattern: "))
L = int(input("Enter the length of the clump: "))
t = int(input("Enter the minimum number of times the pattern must appear in the clump: "))


patterns = []


for i in range(len(string)-L+1):
    clump = string[i:i+L]
    counts = {}
    for j in range(len(clump)-k+1):
        pattern = clump[j:j+k]
        if pattern not in counts:
            counts[pattern] = 0
        counts[pattern] += 1
    for pattern, count in counts.items():
        if count >= t and pattern not in patterns:
            patterns.append(pattern)


print(patterns)