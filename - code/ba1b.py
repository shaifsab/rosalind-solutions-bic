def frequent_words(Text, k):
    freq_map = {}
    n = len(Text)
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        if pattern in freq_map:
            freq_map[pattern] += 1
        else:
            freq_map[pattern] = 1
    max_count = max(freq_map.values())
    return [kmer for kmer in freq_map if freq_map[kmer] == max_count]


Text = input("Enter the string: ")
k = int(input("Enter the value of k: "))


print(frequent_words(Text, k))