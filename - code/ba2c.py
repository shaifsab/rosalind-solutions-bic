def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    max_prob = -1
    for i in range(n-k+1):
        pattern = text[i:i+k]
        prob = 1
        for j in range(k):
            if pattern[j] == 'A':
                prob *= profile[0][j]
            elif pattern[j] == 'C':
                prob *= profile[1][j]
            elif pattern[j] == 'G':
                prob *= profile[2][j]
            elif pattern[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = pattern
    return most_probable_kmer


text = input("Enter the DNA sequence: ")
k = int(input("Enter the length of k-mer: "))
profile = []
for i in range(4):
    row = input(f"Enter the probabilities of {['A','C','G','T'][i]} at each position separated by space: ").split()
    row = [float(x) for x in row]
    profile.append(row)


print(ProfileMostProbableKmer(text,k,profile))