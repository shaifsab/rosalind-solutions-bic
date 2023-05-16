string1 = input("Enter the first DNA string: ")
string2 = input("Enter the second DNA string: ")


hamming_distance = sum([1 for i in range(len(string1)) if string1[i] != string2[i]])


print(hamming_distance)